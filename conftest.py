
import pytest
from playwright.sync_api import sync_playwright
import os


os.makedirs("screenshots", exist_ok=True)

@pytest.fixture(scope="function")
def page(request):
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        
        rep = getattr(request.node, "rep_call", None)
        if rep and rep.outcome == "failed":
            screenshot_path = f"screenshots/{request.node.name}.png"
            page.screenshot(path=screenshot_path)

        browser.close()


@pytest.hookimpl(hookwrapper=True, trylast=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
