import json
import names
import allure
import pytest

# ✅ Explicitly import Squish's test module
from squish import *

source(findFile("scripts", "BookTicket.py"))
source(findFile("scripts", "CommonFunctions.py"))
source(findFile("scripts", "GVariables.py"))

data = data_load(BookTicketJSON)

class TestRailwayBooking:

    @pytest.mark.testcase("Booking Submission")
    def test_booking_submit(self):
        test.startSection("Booking Submission Test")  # ✅ Squish test functions
        try:
            for ticket in data["BookTicket"]:
                test.log(f"Launching application for ticket: {ticket}")
                launch_application(Railway)

                test.log("Filling booking form")
                fill_booking_form(ticket)

                test.log("Saving booking")
                Save_Booking(ticket)

                test.log("Closing application")
                Close_Application(Railway)

            test.passes("Booking submission test passed successfully.")
        except Exception as e:
            test.fail(f"Booking submission test failed: {str(e)}")
        finally:
            test.endSection()

    @pytest.mark.testcase("Cancel Button Functionality")
    def test_cancel_button(self):
        test.startSection("Cancel Button Functionality Test")  # ✅ Squish test functions
        try:
            for ticket1 in data["CancelButton"]:
                test.log(f"Launching application for ticket: {ticket1}")
                launch_application(Railway)

                test.log("Filling booking form")
                fill_booking_form(ticket1)

                test.log("Testing Cancel button functionality")
                Cancel_button_Working()

                test.log("Closing application")
                Close_Application(Railway)

            test.passes("Cancel button functionality test passed successfully.")
        except Exception as e:
            test.fail(f"Cancel button functionality test failed: {str(e)}")
        finally:
            test.endSection()

def main():
    test_suite = TestRailwayBooking()
    test_suite.test_booking_submit()
    test_suite.test_cancel_button()
