import json
import names
import allure
import pytest

# Squish functions are already available in the test environment
source(findFile("scripts", "Login.py"))
source(findFile("scripts", "CommonFunctions.py"))
source(findFile("scripts", "GVariables.py"))

data = data_load(LoginJSON)

class TestRailwayLogin:

    @pytest.mark.testcase("Login Functionality")
    def test_login(self):
        # Using Squish's `test` functions
        test.startSection("Login Functionality Test")
        try:
            for ticket in data["Login"]:
                test.log(f"Launching application")
                launch_application(Railway)

                test.log("Performing login")
                LoginFunctionlity(ticket)

                test.log("Closing application")
                Close_Application(Railway)

            test.passes("Login functionality test passed successfully.")
        except Exception as e:
            test.fail(f"Login functionality test failed: {(e)}")

def main():
    test_suite = TestRailwayLogin()
    test_suite.test_login()
