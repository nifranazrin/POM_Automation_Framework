# 🚀 POM Automation Framework

An **Engineer-Level Automated Testing Framework** built using **Python**, **Selenium**, and **Pytest**. 
This project implements the **Page Object Model (POM)** design pattern to ensure scalability, maintainability, and code reusability.

---

## 🏗️ Architecture

This framework follows the **Page Object Model (POM)** architecture:

-   **Tests Layer:** Contains the actual test scripts (Validations).
-   **Page Layer:** Contains the locators and interactions for each web page.
-   **Core Layer:** Handles the driver initialization and common wrapper methods.
-   **Config Layer:** Centralized location for test data and environments.



### 📂 Folder Structure
```text
POM_Framework/
├── config/            # Test Data & Configurations (URLs, Usernames)
├── pages/             # Page Object Classes (Locators & Actions)
├── tests/             # Test Scripts (Pytest files)
├── utilities/         # Helper functions (Logs, Excel Readers)
├── reports/           # Generated HTML Test Reports
├── venv/              # Virtual Environment
├── .gitignore         # Files excluded from Git
└── requirements.txt   # Project Dependencies



