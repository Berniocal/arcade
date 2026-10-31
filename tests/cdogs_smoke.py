"""Headless browser smoke checks for the original C-Dogs SDL 2.5.0 mobile player."""
from __future__ import annotations

import http.server
import io
import os
from pathlib import Path
import socketserver
import threading
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass

with socketserver.TCPServer(("127.0.0.1", 0), Handler) as server:
    port = server.server_address[1]
    threading.Thread(target=server.serve_forever, daemon=True).start()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path="/usr/bin/google-chrome", args=["--no-sandbox", "--disable-dev-shm-usage", "--enable-unsafe-swiftshader", "--autoplay-policy=no-user-gesture-required"])
        context = browser.new_context(viewport={"width": 844, "height": 390}, is_mobile=True, has_touch=True, device_scale_factor=1)
        page = context.new_page()
        errors = []
        page.on("pageerror", lambda e: errors.append(str(e) + "\n" + str(getattr(e, "stack", ""))))
        page.on("console", lambda m: print("BROWSER CONSOLE:", m.type, m.text, flush=True))
        page.on("requestfailed", lambda r: print("BROWSER REQUEST FAILED:", r.url, r.failure, flush=True))
        page.on("crash", lambda _: errors.append("Chromium page crashed"))
        page.goto(f"http://127.0.0.1:{port}/cdogs.html", wait_until="domcontentloaded")
        assert page.locator("canvas#screen").count() == 1
        assert page.locator('[data-key="ArrowLeft"]').count() == 1
        assert page.locator('[data-key="KeyX"]').count() == 1
        page.locator("#start").click()
        page.wait_for_function("document.getElementById('overlay').hidden === true", timeout=55_000)
        # Native C-Dogs mounts its own /persistent_data after onRuntimeInitialized.
        page.wait_for_function("window.Module && Module.syncdone === 1", timeout=35_000)
        print("GAME SYNC COMPLETE", flush=True)
        image_path = ROOT / "cdogs-smoke-landscape.png"
        colors = 0
        for attempt in range(35):
            data = page.locator("#screen").screenshot(path=str(image_path))
            with Image.open(io.BytesIO(data)) as im:
                # Ignore CSS border, rounded corners and letterboxing:
                # only pixels within the actual game image count.
                w, h = im.size
                interior = im.crop((int(w * .17), int(h * .14), int(w * .83), int(h * .86)))
                colors = len(interior.convert("RGB").getcolors(maxcolors=1_000_000) or [])
            if colors > 12:
                break
            page.wait_for_timeout(1000)
        page.screenshot(path=str(ROOT / "cdogs-smoke-ui.png"))
        print("GAME PIXEL COLORS:", colors, "SYNC:",page.evaluate("Module.syncdone"), flush=True)
        assert not errors, f"Browser errors after game launch: {errors}"
        assert page.evaluate("typeof Module.FS?.syncfs === 'function'"), "Persistent filesystem not exposed"
        assert colors > 12, f"Canvas remained blank/uniform for 35s ({colors} colors)"
        page.evaluate("""
          () => { window.__observedKeys=[];
            document.addEventListener('keydown', e => window.__observedKeys.push(e.code), {capture:true}); }
        """)
        page.locator('[data-key="KeyX"]').tap()
        assert "KeyX" in page.evaluate("window.__observedKeys"), "Touch fire button did not send a keyboard event"
        # Check save-path roundtrip across reload.
        page.evaluate("Module.FS.writeFile('/persistent_data/cdogs-test-save.txt', 'saved from browser')")
        page.locator("#saveBtn").click()
        page.wait_for_function("document.getElementById('status').textContent.includes('uloženy')", timeout=30_000)
        page.reload(wait_until="domcontentloaded")
        page.locator("#start").click()
        page.wait_for_function("document.getElementById('overlay').hidden === true", timeout=55_000)
        page.wait_for_function("window.Module && Module.syncdone === 1", timeout=35_000)
        saved = page.evaluate("""
          () => {
            try { return new TextDecoder().decode(Module.FS.readFile('/persistent_data/cdogs-test-save.txt')); }
            catch(e) { return 'MISSING:' + e; }
          }
        """)
        assert saved == "saved from browser", f"Save was not restored: {saved}"
        page.screenshot(path=str(ROOT / "cdogs-smoke-ui.png"))
        context.close()
        browser.close()
    server.shutdown()
print("PASS: WebAssembly launch, canvas rendering, touch key and IndexedDB save/load")
