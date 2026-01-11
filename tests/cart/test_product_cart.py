import re
from playwright.sync_api import Page, expect

def test_cart_001(page: Page) -> None:
    page.goto("https://sauce-demo.myshopify.com/")
    page.get_by_role("link", name="Grey jacket Grey jacket £").click()
    page.get_by_role("button", name="Add to Cart").click()
    page.get_by_role("button", name="Add to Cart").click()
    page.get_by_role("button", name="Add to Cart").click()
    page.get_by_role("link", name="Catalog").click()
    page.get_by_role("link", name="Check Out").click()
    expect(page.locator("#cart")).to_contain_text("Grey jacket - Grey jacket")
    expect(page.locator("#cart #updates_611945025")).to_have_value("2");
    page.screenshot(path="screenshot.png")


def test_cart_002(page: Page) -> None:
    page.goto("https://sauce-demo.myshopify.com/")
    page.get_by_role("link", name="Grey jacket Grey jacket £").click()
    page.get_by_role("button", name="Add to Cart").click()
    page.get_by_role("button", name="Add to Cart").click()
    page.get_by_role("button", name="Add to Cart").click()
    page.get_by_role("link", name="Catalog").click()
    page.get_by_role("link", name="Check Out").click()
    expect(page.locator("#cart #updates_611945025")).to_have_value("2");
    page.get_by_role("heading", name="Just a demo site showing off").click()
    expect(page.locator("#cart")).to_contain_text("Price")
    expect(page.locator("#cart")).to_contain_text("Qty")
    expect(page.locator("#cart")).to_contain_text("£55.00")
    expect(page.locator("#cart #updates_611945025")).to_have_value("2");
    expect(page.locator("#cart")).to_contain_text("£110.00")
    page.screenshot(path="screenshot.png")
    
    
    

