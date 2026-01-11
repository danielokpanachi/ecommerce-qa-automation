import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://sauce-demo.myshopify.com/")
    page.get_by_role("link", name="Grey jacket Grey jacket £").click()
    page.get_by_role("button", name="Add to Cart").click()
    page.get_by_role("button", name="Add to Cart").click()
    page.get_by_role("link", name="Catalog").click()
    page.get_by_role("link", name="Check Out").click()
    page.get_by_role("link", name="x").click()
    expect(page.locator("#cart")).to_contain_text("It appears that your cart is currently empty! Continue Shopping.")
    page.screenshot(path="screenshot.png")


# import pytest
# from playwright.sync_api import Page, expect
# from pages.product_details_page import ProductDetailsPage


# def test_add_and_remove_product_from_cart(page: Page) -> None:
#     # Initialize page object
#     product_page = ProductDetailsPage(page)
    
#     # Navigate to home and select product
#     product_page.navigate_to("/")
#     page.get_by_role("link", name="Grey jacket Grey jacket £").click()
    
#     # Add product to cart twice using POM method
#     product_page.click_add_to_cart()
#     product_page.click_add_to_cart()
    
#     # Navigate using role locators (easier for now)
#     page.get_by_role("link", name="Catalog").click()
#     page.get_by_role("link", name="Check Out").click()
#     page.get_by_role("link", name="x").click()
    
#     # Verify cart is empty
#     expect(page.locator("#cart")).to_contain_text(
#         "It appears that your cart is currently empty! Continue Shopping."
#     )