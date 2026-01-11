Manual Test Execution – E-Commerce Checkout

1 Product Listing Page - Test Cases

    TC-PLP-001
    Status: PASS
    Reason: Page loads without errors and one product card is visible

    TC-PLP-002
    Status: PASS
    Reason: Product name is visible, product price is visible and add to cart button is enabled

    TC-PLP-003
    Status: N/A
    Reason: Price sorting OUT OF SCOPE


2 Product Details Page - Test Cases

    TC-PDP-001
    Status: PASS
    Reason: Product name matches PLP , product price matches PLP

    TC-PDP-002
    Status: PASS 
    Reason: Quantity cannot be less than 1, cart becomes empty.


3 Product Cart - Test Cases

    TC-CART-001
    Status: PASS
    Reason: Product appears inside cart and quantity is correct

    TC-CART-002
    Status: PASS
    Reason: Line total is price * quantity, subtotal is accurate

    TC-CART-003
    Status: PASS 
    Reason: Product removed, card subtotal is updated, cart becomes empty without message


4 Product Checkout - Test Cases

    TC-CHK-001
    Status: N/A
    Reason: Checkout has no requirements to be left empty 

    TC-CHK-002
    Status: N/A
    Reason: OUT OF SCOPE


5 Product Payment Verification - Test Cases 

    TC-PAY-001
    Status: PASS
    Reason: Pay/place order button does not work if card details are invalid

    TC-PAY-002
    Status: N/A
    Reason: No sandbox payment available 


6 Product Shipping -Test Cases

    TC-SHIP-001
    Status: PASS
    Reason: Available shipping methods on display

    TC-SHIP-002
    Status: PASS
    Reason: Order total updates accordingly


7 Product Order Confirmation - Test Cases

    TC-CONF-001
    Status: N/A
    Reason: No sandbox payment available so not able to progress order to confirmation 


    Authentication : OUT OF SCOPE 