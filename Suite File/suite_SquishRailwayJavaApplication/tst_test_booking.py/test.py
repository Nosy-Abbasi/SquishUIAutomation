import json
import names
import allure
import pytest

source(findFile("scripts", "BookTicket.py"))
source(findFile("scripts", "CommonFunctions.py"))
source(findFile("scripts", "GVariables.py"))


def main():

    allure.suite("Booking Functionality")

    data = data_load(BookTicketJSON)

    
    def test_booking_submit():
        for ticket in data["BookTicket"]:
                launch_application(Railway)  
                fill_booking_form(ticket)
                Save_Booking(ticket)
            
    
    
    def test_cancel_button():
        for ticket1 in data["CancleButton"]:
                launch_application(Railway)
                fill_booking_form(ticket1)
                Cancel_button_Working()  

    allure.testcase("Test101", "Booking Submit")
    test_booking_submit()
    allure.testcase("Test102", "Booking Cancel")
    test_cancel_button()
