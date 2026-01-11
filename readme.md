# E-Commerce Demo QA Automation

##  Project Description
This project automates key functionalities of a demo e-commerce site ([https://sauce-demo.myshopify.com/](https://sauce-demo.myshopify.com/)) 
using **Playwright** and **Python**. 

It includes automated tests for:
- Product Listing Page (PLP)
- Product Details Page (PDP)
- Cart functionalities (add/remove items, quantity validation)

Additionally, the project generates **HTML reports** and **failure screenshots** to provide clear test results.

---

##  Scope

### Automated:
- Product Listing Page (PLP)
- Product Details Page (PDP)
- Cart functionality:
  - Add to Cart
  - Remove from Cart
  - Quantity validation
  - Cart total validation

### Not Automated / Out of Scope:
- Login (captcha on demo site)
- Checkout / payment (no sandbox available)
- Advanced filtering/sorting (site limitations)

---

## Folder Structure
project_root/
├── pages/ # Page Object files
│ ├── base_page.py
│ └──product_details_page.py
│ 
├── tests/ # Automated test files
│ ├── auth/
│ ├── cart/
│ ├── details/
│ └── plp/
├── test_data/ # JSON/YAML files for test data
├── reports/ # HTML reports
├── screenshots/ # Screenshots of failed tests
├── conftest.py # Pytest fixtures
├── requirements.txt # Python dependencies
└── README.md # Project documentation

##  Setup / Installation

 Clone the repository:
```bash

git clone <repo_url>
cd <project_root>
python -m venv venv
# Mac/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
pip install -r requirements.txt
playwright install
pytest
pytest --html=reports/report.html
pytest tests/cart/test_cart.py

Limittions
This is a demo site; some features (login, checkout) are not automated due to captcha / no sandbox.
Quantity input IDs are hardcoded from the demo site and may change.


---
 Author / Contact
Your Daniel Okpanachi
Email: kingdan65@gmail.com
GitHub: https://github.com/danielokpanachi
LinkedIn: https://linkedin.com/in/danielokpanachi