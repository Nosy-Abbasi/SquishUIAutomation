# -*- coding: utf-8 -*-  
import json
from squish import *
import sys
import os
import LoginLocators


def LoginFunctionlity(data):
    
    Click(LoginLocators.admin_Login,"Booking button")
    
    Enter_Text(LoginLocators.Admin_ID,data["Admin ID"])
    
    Enter_Text(LoginLocators.Password,data["Password"])
    
    Click(LoginLocators.Login,"Login Button")
    
    Text_Verification(LoginLocators.Wrong_Username_Password,data["Expected Message"])
    
