
# import pytest
# from playwright.sync_api import sync_playwright

# @pytest.fixture(scope="function")
# def page():
#     """
#     This fixture provides a fresh Playwright page object for each test.
#     - Opens a Chromium browser
#     - Gives the test a `page` to work with
#     - Closes browser after test
#     """
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)  # set True if you don't want browser window
#         page = browser.new_page()
#         yield page
#         browser.close()


import pytest
from playwright.sync_api import sync_playwright
import os

# Ensure screenshots folder exists
os.makedirs("screenshots", exist_ok=True)

@pytest.fixture(scope="function")
def page(request):
    """
    Provides a fresh Playwright page for each test.
    Captures screenshot on failure.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        # Check if test failed
        if request.node.rep_call.failed:
            test_name = request.node.name
            screenshot_path = f"screenshots/{test_name}.png"
            page.screenshot(path=screenshot_path)
        browser.close()

# Hook to mark test outcome
def pytest_runtest_makereport(item, call):
    # Store result on the test node for fixture access
    if "page" in item.fixturenames:
        setattr(item, "rep_" + call.when, call)
