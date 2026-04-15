# Automation Exercise - Pytest Selenium Framework

## Project Overview

**Automation Exercise** is a test automation project designed to practice end-to-end UI testing for an e-commerce application.

This project focuses on automating a core user journey to simulate real-world testing scenarios. It is intended for learning, practice, and demonstrating automation skills.

---

## Tech Stack

* Python
* Pytest
* Selenium WebDriver
* Allure Reports
* Black (code formatter)

---

## Project Setup

### 🔹 1. Install Python

Ensure Python (3.9 or above) is installed:

```bash
python3 --version
```

---

### 🔹 2. Clone Repository

```bash
git clone <automation-exercise-repo-url>
cd automation-exercise
```

---

### 🔹 3. Create Virtual Environment

```bash
python3 -m venv venv
```

Activate it:

**Mac/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

---

### 🔹 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 5. Install Allure (Reporting Tool)

#### Mac (using Homebrew)

```bash
brew install allure
```

#### Windows (using Scoop)

```bash
scoop install allure
```

Verify installation:

```bash
allure --version
```

---

## Running Tests

### Run all tests:

```bash
pytest
```

---

### Run tests with Allure results:

```bash
pytest --alluredir=reports/allure-results
```

---

### Generate Allure Report:

```bash
allure serve reports/allure-results
```

---

### Run a specific test file:

```bash
pytest -s -v {path to test file} --alluredir=./output/allure
```

* `-s` → shows print/log output in console
* `-v` → enables verbose (detailed) test output
* `--alluredir` → stores Allure results for reporting

---

## Code Formatting

This project uses **Black** for consistent code formatting.

### Format code:

```bash
black .
```

---

## Project Structure

```text
automation-exercise/
│
├── assets/ # (Optional/Future) assets for file uploads
├── lang/                  # Localization / translation support
│   └── en/                # English language files
│       └── *.json / *.py  # Translation keys/values
│
├── pages/                 # Page Object Models (POM)
├── reports/               # Stores test reports (Allure, HTML, etc.)
├── tests/
│   ├── ui/
│   │   ├── user/          # End-user test scenarios (e.g., shopping flow)
│   │   └── admin/         # Admin panel UI tests (future/extendable)
│   │
│   └── api/               # (Optional/Future) API test cases
│
├── utils/                 # Utilities (helpers, etc.)
│
├── conftest.py            # Pytest fixtures
├── pytest.ini             # Pytest configuration
├── requirements.txt       # Project dependencies
└── README.md
```

---

## Localization Support

The `lang/` directory is designed to support **multi-language testing**.

* Currently includes:

  * `en/` → English translations
* Easily extendable:

  * `fr/` → French
  * `ar/` → Arabic
  * `ur/` → Urdu

Useful for validating UI text across different locales.

---

## Test Organization Strategy

* `tests/ui/user/` → Covers **end-user journeys** (current scope)
* `tests/ui/admin/` → Reserved for **admin panel testing**
* `tests/api/` → Can be added later for API automation

This structure keeps tests **modular, scalable, and clean**

---

## Notes

* Uses **Pytest fixtures** for driver and configuration management
* Supports **headless execution** via CLI
* Easily extendable for:

  * More test scenarios
  * Multi-browser support
  * CI/CD integration

---

## Future Enhancements

* Integrate CI/CD (GitHub Actions)
* Add parallel execution (pytest-xdist)
* Enhance reporting with screenshots/logs
* Cover authentication flow (login, signup)

---

## Author

Automation practice project for learning and demonstrating QA automation skills.
