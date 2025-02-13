# -*- coding: utf-8 -*-  
import json
from squish import *
import sys
import os

names_path = r"C:\Users\SpanIdea\OneDrive\Desktop\Squish Automation\Suite File\suite_SquishRailwayJavaApplication\shared\scripts"

import names

def fill_booking_form(data):
    # Fill out the booking form with data
    mouseClick(waitForObjectExists(names.book_Tickets_JButton))
    test.log("Button Clicked - Book Tickets")

    type(waitForObject(names.booking_Panel_Full_Name_JTextArea), data["FullName"])
    test.log("Entered text - Full Name")

    type(waitForObject(names.booking_Panel_Email_Id_JTextArea), data["Email"])
    test.log("Entered text - Email ID")

    mouseClick(waitForObjectExists(names.booking_Panel_Day_JRadioButton))
    test.log("Button Clicked - Shift Day")

    type(waitForObject(names.booking_Panel_Time_JTextArea), data["Time"])
    test.log("Entered text - Time")

    type(waitForObject(names.booking_Panel_Train_Name_JTextArea), data["Train Name"])
    test.log("Entered text - Train Name")

    type(waitForObject(names.booking_Panel_Starting_From_JTextArea), data["Starting From"])
    test.log("Entered text - Starting From")

    type(waitForObject(names.booking_Panel_Destination_JTextArea), data["Destination"])
    test.log("Entered text - Destination")

    mouseClick(waitForObjectExists(names.booking_Panel_Add_JButton))
    test.log("Button Clicked - Add")

    mouseClick(waitForObjectExists(names.select_an_Option_Yes_JButton))
    test.log("Button Clicked - Yes")

def verify_booking(Expected_Message):
    # Verify if the ticket booking is successful
    Actual_Message = waitForObjectExists(names.message_Ticket_is_booked_sucessfully_JLabel).text
    test.log(f"{Actual_Message}")

    if Expected_Message in Actual_Message:
        test.passes("Test Passed")
    else:
        test.log(f"Test Failed: Expected '{Expected_Message}', but got '{Actual_Message}'"); saveDesktopScreenshot("FailedScreen.png"); test.fail("Test Failed")
        

