# from pages.basepage import BasePage


# class ProductDetailsPage(BasePage):
#     """Product Details Page Object for sauce-demo.myshopify.com"""
    
#     # Locators
#     PRODUCT_TITLE = "h1.product-single__title"
#     PRODUCT_PRICE = ".product-single__price"
#     PRODUCT_IMAGE = ".product-single__photo img"
#     PRODUCT_DESCRIPTION = ".product-single__description"
    
#     SIZE_SELECTOR = "select#product-select-option-0"
#     COLOR_SELECTOR = "select#product-select-option-1"
#     QUANTITY_INPUT = "input[type='number'][name='quantity']"
    
#     ADD_TO_CART_BUTTON = "button[type='submit'][name='add']"
#     BUY_NOW_BUTTON = ".shopify-payment-button__button"
    
#     CART_LINK = "a[href='/cart']"
#     CART_COUNT = ".cart-link__bubble"
    
#     PRODUCT_VENDOR = ".product-single__vendor"
#     PRODUCT_TYPE = ".product-single__type"
#     PRODUCT_SKU = ".product-single__sku"
    
#     # Methods
#     def get_product_title(self) -> str:
#         """Get the product title"""
#         return self.get_text(self.PRODUCT_TITLE)
    
#     def get_product_price(self) -> str:
#         """Get the product price"""
#         return self.get_text(self.PRODUCT_PRICE)
    
#     def get_product_description(self) -> str:
#         """Get the product description"""
#         return self.get_text(self.PRODUCT_DESCRIPTION)
    
#     def select_size(self, size: str):
#         """Select product size"""
#         if self.is_visible(self.SIZE_SELECTOR):
#             self.page.locator(self.SIZE_SELECTOR).select_option(label=size)
    
#     def select_color(self, color: str):
#         """Select product color"""
#         if self.is_visible(self.COLOR_SELECTOR):
#             self.page.locator(self.COLOR_SELECTOR).select_option(label=color)
    
#     def set_quantity(self, quantity: int):
#         """Set product quantity"""
#         self.fill(self.QUANTITY_INPUT, str(quantity))
    
#     def get_quantity(self) -> int:
#         """Get current quantity value"""
#         value = self.page.locator(self.QUANTITY_INPUT).input_value()
#         return int(value)
    
#     def click_add_to_cart(self):
#         """Click Add to Cart button"""
#         self.click(self.ADD_TO_CART_BUTTON)
    
#     def is_add_to_cart_enabled(self) -> bool:
#         """Check if Add to Cart button is enabled"""
#         return self.is_enabled(self.ADD_TO_CART_BUTTON)
    
#     def get_cart_count(self) -> int:
#         """Get cart item count"""
#         if self.is_visible(self.CART_COUNT):
#             count_text = self.get_text(self.CART_COUNT)
#             return int(count_text)
#         return 0
    
#     def go_to_cart(self):
#         """Navigate to cart page"""
#         self.click(self.CART_LINK)
    
#     def add_product_to_cart(self, quantity: int = 1, size: str = None, color: str = None):
#         """Complete flow to add product to cart"""
#         if size:
#             self.select_size(size)
#         if color:
#             self.select_color(color)
#         if quantity > 1:
#             self.set_quantity(quantity)
#         self.click_add_to_cart()
#         self.wait_for_element(self.CART_COUNT)
    
#     def verify_product_loaded(self):
#         """Verify product page is fully loaded"""
#         self.assert_visible(self.PRODUCT_TITLE)
#         self.assert_visible(self.PRODUCT_PRICE)
#         self.assert_visible(self.ADD_TO_CART_BUTTON)