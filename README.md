# Squish Hybrid Automation Framework

A hybrid test automation framework built using [Squish](https://www.froglogic.com/squish/) for Java-based desktop applications. This framework combines the **Data-Driven** approach with the **Page Object Model (POM)** to achieve modularity, reusability, and scalability. It supports execution on **Windows** and **macOS**, and uses **JSON** files for test data management.



## Table of Contents

- [Features]
- [Tech Stack]
- [Prerequisites]
- [Installation]
- [Project Structure]
- [How to Use]
- [Test Data Management]
- [Page Object Model (POM) Approach]
- [Test Suites]
- [Contribution]
- [Support]

---

## Features

- Hybrid framework combining Data-Driven + Page Object Model
- Reusable custom functions
- Structured test suites: Sanity, Smoke, Regression
- JSON-based test data management
- Easy test execution with Squish command-line and IDE
- Logging and reporting included

---

## Tech Stack

- **Language**: Python (Squish scripting language)
- **Tool**: [Squish](https://www.froglogic.com/squish/)
- **Framework Type**: Hybrid (Data-Driven + POM)
- **Target Application**: Java Swing Desktop Application
- **Data Format**: JSON

---

## Prerequisites

- Squish 8.1.0 or above
- Python 3.x (if using external scripts)
- Java Runtime Environment (JRE) to run the AUT
- License for Squish (evaluation or commercial)
- Access to the Java Swing application under test (AUT)

---

## Installation

1. **Install Squish**
   - Download and install from [Squish Downloads](https://www.froglogic.com/squish/download/)
   - Choose the Java edition.

2. **Configure Your Application Under Test (AUT)**
   - Use the Squish IDE to attach and configure the AUT.

3. **Clone this Repository**
   ```bash
   git clone https://github.com/yourusername/squish-java-hybrid-framework.git
   cd squish-java-hybrid-framework

## Project Structure

squish-java-hybrid-framework/
│
├── Reports/
│   ├── Allure Report
│   ├── ScreenShot on Failure
├── Scripts/
│   ├── CommonFucntions
│   ├── DataFile
│   ├── FucntionFile
│   ├── GlobalVariables
│   ├── Locators
├── SuiteFile/
│   ├── RegressionSuite
│   ├── Smoke
└── README.md

## How to Use

Run from Squish IDE:
Open Squish IDE

Import suite (e.g. suite_regression)

Click on Run Test Suite

Run from CLI:
squishrunner --testsuite suites/suite_regression --reportgen xml3.5,report_folder


## Test Data Management

Test data is stored in JSON format under /testData/.
A utility is used to read test data dynamically during execution.

{
  "valid_user": {
    "username": "admin",
    "password": "admin123"
  },
  "invalid_user": {
    "username": "user",
    "password": "wrongpass"
  }
}


## Page Object Model (POM) Approach

Locators are defined inside Scripts/Locators/
Business Logic functions are placed inside Scripts/FucntionFile/
Common reusable functions go into Scripts/CommonFucntions/
Global settings or variables in Scripts/GlobalVariables/


## Test Suites

Smoke Tests: SuiteFile/Smoke
Regression Tests: SuiteFile/RegressionSuite
Each suite contains:
.test files for test cases
test.py (or appropriate scripting file) for logic

## Contribution

Contributions are welcome! Please ensure:
Code is modular and follows the existing structure
Tests are written with data-driven and POM principles in mind
Proper documentation is included with new features

## Support
If you encounter issues or have questions, feel free to raise an issue or contact the maintainer.

