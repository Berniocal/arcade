#!/usr/bin/env python3
"""Small browser smoke test for the standalone Age of War web game."""
from contextlib import contextmanager
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import os
import threading
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]

@contextmanager
def serve():
    os.chdir(ROOT)
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), SimpleHTTPRequestHandler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    try:
        yield "http://127.0.0.1:" + str(httpd.server_port)
    finally:
        httpd.shutdown()
        httpd.server_close()

def smoke(page, url, screenshot):
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.goto(url, wait_until="domcontentloaded")
    page.wait_for_selector("#start", state="visible")
    assert "Age of War" in page.title()
    page.locator("#start").click()
    page.wait_for_function("document.querySelector('#overlay').hidden")
    assert "300" in page.locator("#money").inner_text()
    assert page.locator("#cards .buy").count() == 3
    page.locator("#cards .buy").first.click()
    assert "Lovec" in page.locator("#queue").inner_text()
    page.wait_for_timeout(2100)
    assert "žádná jednotka" in page.locator("#queue").inner_text()
    page.locator('[data-tab="towers"]').click()
    assert page.locator("#cards .buy").count() == 3
    page.locator("#pauseBtn").click()
    assert page.locator("#resume").is_visible()
    page.locator("#resume").click()
    page.locator("#special").click()
    assert page.locator("#special").is_disabled()
    page.locator("#soundBtn").click()
    assert "🔇" in page.locator("#soundBtn").inner_text()
    page.locator("#rightCam").click()
    assert page.locator("#followCam").get_attribute("aria-pressed") == "false"
    assert page.locator("#field").evaluate("(el)=>el.width>0 && el.height>0")
    page.screenshot(path=screenshot, full_page=True)
    assert not errors, errors

with serve() as base:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path=os.getenv("CHROME", "/usr/bin/google-chrome"), args=["--no-sandbox"])
        try:
            desktop = browser.new_page(viewport={"width": 1100, "height": 780})
            smoke(desktop, base + "/age-of-war.html", "age-of-war-desktop.png")
            desktop.close()
            mobile = browser.new_page(viewport={"width": 390, "height": 844}, has_touch=True, is_mobile=True)
            smoke(mobile, base + "/age-of-war.html", "age-of-war-mobile.png")
            mobile.close()
            directory = browser.new_page()
            directory.goto(base + "/index.html")
            assert directory.locator('[data-game="ageofwar"]').count() == 1
            directory.locator('[data-game="ageofwar"]').click()
            assert directory.locator("#gameFrame").get_attribute("src") == "age-of-war.html"
            directory.close()
            print("Age of War smoke OK (desktop, mobile, arcade integration)")
        finally:
            browser.close()
