# Hybrid QA Automation Framework (Playwright + Pytest)

This repository contains the professional and scalable base architecture of a hybrid automation framework designed for both Frontend (UI) and Backend (API) testing. It is fully decoupled, dynamic, and ready for CI/CD integration.

## 🚀 Key Features
- **Pure Hybrid Approach:** Efficient test data management (creation during `SETUP` and cleanup during `TEARDOWN` via API endpoints) combined with complex user interface actions.
- **Page Object Model (POM):** Clean structure that encapsulates UI selectors and interactions.
- **Multi-Environment Configuration:** Dynamic implementation based on environment variables (`.env`) and centralized logic via `config.py`.
- **Advanced Allure Reporting:** Smart reporting that automatically attaches full-page screenshots and interactive videos *only* when a test case fails.

---

## 📁 Project Structure

```text
com_theinternet_qa_framework/
│
├── .env                          # Local environment file with URLs and credentials (Excluded from Git)
├── .gitignore                    # Git ignore file to filter folders (venv/, allure-results/, .env)
├── config.py                     # Centralizes environment variables using python-dotenv
├── pytest.ini                    # Global Pytest configuration and execution directives
├── requirements.txt              # Project dependencies (pytest, playwright, allure-pytest, etc.)
│
├── api/                          # Backend automation layer (API Testing)
│   ├── __init__.py
│   └── user_api.py               # HTTP controllers (POST, DELETE) for fast data injection
│
├── pages/                        # UI layer under Page Object Model (POM) pattern
│   ├── __init__.py
│   └── login_page.py             # Login Page abstraction (selectors and user actions)
│
├── tests/                        # Orchestration and Test Cases layer
│   ├── __init__.py
│   ├── conftest.py               # Global fixtures (data lifecycles) and Hooks for Allure
│   └── test_login.py             # Executable test scripts for the automated flow
│
└── allure-results/               # Raw results generated after test runs (JSON, videos, images)
```
---

## 🛠️ Tech Stack & Dependencies
- **Python 3**
- **Playwright** (Fast and modern web automation)
- **Pytest** (Robust test runner)
- **Allure Report** (Interactive dashboards and execution analytics)
- **Python-dotenv** (Environment variables management)


## 🔧 Initial Setup

### 1. Clone the repository and navigate to the project root:

```Bash
cd com_theinternet_qa_framework
```

### 2. Create and activate a virtual environment (venv):

```Bash
python -m venv venv
source venv/Scripts/activate  # On Windows (Git Bash)
```
### 3. Install dependencies and browser binaries:

```Bash
pip install -r requirements.txt
playwright install
```

### 4. Configure environment variables:
Create a .env file in the root directory based on the variables mapped in config.py.

## 🚦 Running Tests and Reports
Run all tests:

```Bash
pytest
Run with detailed output (verbose):
```

```Bash
pytest -v -s
Generate and open the Allure Report:
```

```Bash
pytest --alluredir=allure-results
allure serve allure-results
```