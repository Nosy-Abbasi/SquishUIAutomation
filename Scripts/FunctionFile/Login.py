# -*- coding: utf-8 -*-  
import json
from squish import *
import sys
import os


import names

def Login(data):
    
    mouseClick(waitForObjectExists(names.admin_Login_JButton))
    test.log("Button Clicked - Admin Login")

    type(waitForObject(names.admin_Login_Admin_ID_JTextField), data["Admin ID"])
    test.log("Entered text - Admin ID")
    
    type(waitForObject(names.admin_Login_Password_JPasswordField), data["Password"])
    test.log("Entered text - Password")
    
    mouseClick(waitForObjectExists(names.admin_Login_Login_JButton))
    test.log("Button Clicked - Login")
    
def verify_login(Expected_Message):
    # Verify if the ticket booking is successful
    Actual_Message = waitForObjectExists(names.message_Wrong_Username_Password_JLabel).text
    test.log(f"{Actual_Message}")

    if Expected_Message in Actual_Message:
        test.passes("Test Passed")
    else:
        test.log(f"Test Failed: Expected '{Expected_Message}', but got '{Actual_Message}'"); saveDesktopScreenshot("FailedScreen.png"); test.fail("Test Failed")