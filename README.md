# Playwright SauceDemo Test Automation

## Overview
This project is an end-to-end UI test automation suite for a web-based e-commerce application (SauceDemo). It validates core user workflows including authentication, inventory interaction, cart functionality, and checkout navigation using Python, Playwright, and Pytest.

The test suite is designed using the Page Object Model (POM) to ensure maintainability, scalability, and clear separation of concerns.

---

## Tech Stack
- Python  
- Playwright (UI automation)  
- Pytest (test framework)  

---

## Features Covered
- User login validation (positive and negative scenarios)  
- Inventory interactions (add/remove items, sorting)  
- Cart functionality (item validation, quantity, pricing)  
- Navigation flows (continue shopping, checkout)  
- End-to-end cart workflow validation  

---

## Project Structure

- **pages/**
  - login_page.py
  - inventory_page.py
  - cart_page.py

- **tests/**
  - test_login.py
  - test_inventory.py
  - test_cart.py

- **root**
  - requirements.txt
  - pytest.ini
  - README.md

 ---

## Key Design Decisions
- **Page Object Model (POM):** Encapsulates UI interactions for reusability and cleaner test logic  
- **Data-driven validation:** Uses structured expected data for verifying UI elements  
- **Test isolation:** Each test independently sets up its required state  
- **Scoped locators:** Reduces flakiness by limiting selector scope  
