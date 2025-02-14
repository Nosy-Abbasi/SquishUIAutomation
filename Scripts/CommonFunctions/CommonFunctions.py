# -*- coding: utf-8 -*-  
import json
from squish import *
import sys
import os

def launch_application(AppName):
    # Start the application
    startApplication(AppName)
    snooze(0.3)
    test.log("App Launch Successfully")
    
def Enter_Text(Location,Value):
    type(waitForObject(Location), Value)
    test.log(f"Entered text as - '{Value}'")
    
def Click(Location,Name):
    mouseClick(waitForObjectExists(Location))
    test.log(f"Button Clicked as - '{Name}'")
    
def Text_Verification(Location,Expected_Message):
    Actual_Message = waitForObjectExists(Location).text
    test.log(f"{Actual_Message}")

    if Expected_Message in Actual_Message:
        test.passes("Test Passed")
    else:
        test.log(f"Test Failed: Expected '{Expected_Message}', but got '{Actual_Message}'"); saveDesktopScreenshot("FailedScreen.png"); test.fail("Test Failed")
    
