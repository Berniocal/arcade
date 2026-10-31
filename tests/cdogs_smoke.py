"""Headless browser smoke checks for the original C-Dogs SDL 2.5.0 mobile player."""
from __future__ import annotations

import http.server
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
        browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage", "--autoplay-policy=no-user-gesture-required"])
        context = browser.new_context(viewport={"width": 844, "height": 390}, is_mobile=True, has_touch=True, device_scale_factor=1)
        page = context.new_page()
        errors = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.goto(f"http://127.0.0.1:{port}/cdogs.html", wait_until="domcontentloaded")
        assert page.locator("canvas#screen").count() == 1
        assert page.locator('[data-key="ArrowLeft"]').count() == 1
        assert page.locator('[data-key="KeyX"]').count() == 1
        page.locator("#start").click()
        page.wait_for_function("document.getElementById('overlay').hidden === true", timeout=180_000)
        page.wait_for_timeout(5000)
        assert not errors, f"Browser errors after game launch: {errors}"
        assert page.evaluate("typeof Module.FS?.syncfs === 'function'"), "Persistent filesystem not exposed"
        image_path = ROOT / "cdogs-smoke-landscape.png"
        page.locator("#screen").screenshot(path=str(image_path))
        with Image.open(image_path) as im:
            # A launched game menu has a meaningful variety of colors;
            # a uniform canvas means that the launcher alone was loaded.
            assert len(im.convert("RGB").getcolors(maxcolors=1_000_000) or []) > 12, "Canvas is blank/uniform after launch"
        page.evaluate("""
          () => { window.__observedKeys=[];
            document.addEventListener('keydown', e => window.__observedKeys.push(e.code), {capture:true}); }
        """)
        page.locator('[data-key="KeyX"]').tap()
        assert "KeyX" in page.evaluate("window.__observedKeys"), "Touch fire button did not send a keyboard event"
        # Check save-path roundtrip across reload.
        page.evaluate("Module.FS.writeFile('/home/web_user/cdogs-test-save.txt', 'saved from browser')")
        page.locator("#saveBtn").click()
        page.wait_for_function("document.getElementById('status').textContent.includes('uloženy')", timeout=30_000)
        page.reload(wait_until="domcontentloaded")
        page.locator("#start").click()
        page.wait_for_function("document.getElementById('overlay').hidden === true", timeout=180_000)
        saved = page.evaluate("""
          () => {
            try { return new TextDecoder().decode(Module.FS.readFile('/home/web_user/cdogs-test-save.txt')); }
            catch(e) { return 'MISSING:' + e; }
          }
        """)
        assert saved == "saved from browser", f"Save was not restored: {saved}"
        page.screenshot(path=str(ROOT / "cdogs-smoke-ui.png"))
        context.close()
        browser.close()
    server.shutdown()
print("PASS: WebAssembly launch, canvas rendering, touch key and IndexedDB save/load")
