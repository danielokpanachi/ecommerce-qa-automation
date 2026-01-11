# from playwright.sync_api import Page, expect


# class BasePage:
#     """Base Page Object Model for sauce-demo.shopify.com"""
    
#     def __init__(self, page: Page):
#         self.page = page
#         self.base_url = "https://sauce-demo.myshopify.com/" 
    
#     # Navigation
#     def navigate_to(self, path: str = ""):
#         """Navigate to a specific path"""
#         self.page.goto(f"{self.base_url}{path}")
#         self.page.wait_for_load_state("networkidle")
    
#     def get_current_url(self) -> str:
#         """Get current URL"""
#         return self.page.url
    
#     # Interactions
#     def click(self, locator: str):
#         """Click an element"""
#         self.page.locator(locator).click()
    
#     def fill(self, locator: str, text: str):
#         """Fill text into input field"""
#         self.page.locator(locator).fill(text)
    
#     def get_text(self, locator: str) -> str:
#         """Get text from element"""
#         element = self.page.locator(locator)
#         element.wait_for(state="visible", timeout=10000)
#         return element.text_content().strip()
    
#     def get_attribute(self, locator: str, attribute: str) -> str:
#         """Get attribute value"""
#         return self.page.locator(locator).get_attribute(attribute)
    
#     # State checks
#     def is_visible(self, locator: str) -> bool:
#         """Check if element is visible"""
#         return self.page.locator(locator).is_visible()
    
#     def is_enabled(self, locator: str) -> bool:
#         """Check if element is enabled"""
#         return self.page.locator(locator).is_enabled()
    
#     # Waits
#     def wait_for_element(self, locator: str, state: str = "visible"):
#         """Wait for element"""
#         self.page.locator(locator).wait_for(state=state)
    
#     # Assertions
#     def assert_text_contains(self, locator: str, text: str):
#         """Assert element contains text"""
#         expect(self.page.locator(locator)).to_contain_text(text)
    
#     def assert_visible(self, locator: str):
#         """Assert element is visible"""
#         expect(self.page.locator(locator)).to_be_visible()