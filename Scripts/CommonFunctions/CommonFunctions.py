# -*- coding: utf-8 -*-  
import json
from squish import *
import sys
import os
source(findFile("scripts", "GVariables.py"))


def data_load(FileName):
    json_file_path = FileName
    
    with open(json_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data
    
def launch_application(AppName):
    try:
        # Start the application
        startApplication(AppName)
        snooze(0.3)
        test.log("App Launch Successfully")
    except Exception as e:
        screenshot_folder = r"C:\Users\SpanIdea\OneDrive\Desktop\Squish Automation\Reports\screenshot_folder"
        screenshot_path = os.path.join(screenshot_folder, "App_Launch_Failed.png")
        saveDesktopScreenshot(screenshot_path)
        test.fatal(f"Error occurred while launching the application: {e}")
        raise

    
def Enter_Text(Location,Value):
    try:
        type(waitForObject(Location), Value)
        test.log(f"Entered text as - '{Value}'")
    except Exception as e:
        screenshot_folder = r"C:\Users\SpanIdea\OneDrive\Desktop\Squish Automation\Reports\screenshot_folder"
        screenshot_path = os.path.join(screenshot_folder, "Step_Failed.png")
        saveDesktopScreenshot(screenshot_path)
        test.fatal(f"Step Failed: {e}")
        raise
    
def Click(Location,Name):
    try:
        mouseClick(waitForObjectExists(Location))
        test.log(f"Button Clicked as - '{Name}'")
    except Exception as e:
        screenshot_folder = r"C:\Users\SpanIdea\OneDrive\Desktop\Squish Automation\Reports\screenshot_folder"
        screenshot_path = os.path.join(screenshot_folder, "Step_Failed.png")
        saveDesktopScreenshot(screenshot_path)
        test.fatal(f"Step Failed:: {e}")
        raise
        
def Text_Verification(Location,Expected_Message):
    try: 
        Actual_Message = waitForObjectExists(Location).text
        test.log(f"{Actual_Message}")

        if Expected_Message in Actual_Message:
            test.passes("Test Passed")
        else:
            test.log(f"Test Failed: Expected '{Expected_Message}', but got '{Actual_Message}'");
            screenshot_folder = r"C:\Users\SpanIdea\OneDrive\Desktop\Squish Automation\Reports\screenshot_folder"
            screenshot_path = os.path.join(screenshot_folder, "Assertion_Failed.png")
            saveDesktopScreenshot(screenshot_path) 
            test.fail("Test Failed")
    except Exception as e:
        screenshot_folder = r"C:\Users\SpanIdea\OneDrive\Desktop\Squish Automation\Reports\screenshot_folder"
        screenshot_path = os.path.join(screenshot_folder, "Assertion_Failed_Locator.png")
        saveDesktopScreenshot(screenshot_path)
        test.fatal(f"Assertion Failed due to locator: {e}")
        raise
