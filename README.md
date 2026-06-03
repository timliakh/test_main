## Project structure

```
test_main/
├── conftest.py          # browser fixture, --language option
├── pytest.ini           # pytest markers
├── requirements.txt
├── test_main_page.py    # main page tests
├── test_product_page.py # product page tests
└── pages/
    ├── base_page.py     # shared methods (waits, basket, auth)
    ├── main_page.py     # main page actions
    ├── product_page.py  # product page actions
    ├── login_page.py    # login and registration
    ├── basket_page.py   # basket assertions
    └── locators.py      # element locators
```
