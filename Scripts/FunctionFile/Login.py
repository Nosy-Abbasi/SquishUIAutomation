# -*- coding: utf-8 -*-  
import json
from squish import *
import sys
import os

source(findFile("scripts", "LoginLocator.py"))


def LoginFunctionlity(data):
    
    Click(admin_Login,"Booking button")
    
    Enter_Text(Admin_ID,data["Admin ID"])
    
    Enter_Text(Password,data["Password"])
    
    Click(Login,"Login Button")
    
    Text_Verification(Wrong_Username_Password,data["Expected Message"])
    
