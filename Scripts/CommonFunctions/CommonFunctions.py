# -*- coding: utf-8 -*-  
import json
from squish import *
import sys
import os

names_path = r"C:\Users\SpanIdea\OneDrive\Desktop\Squish Automation\Suite File\suite_SquishRailwayJavaApplication\shared\scripts"

import names

def launch_application():
    # Start the application
    startApplication("railway.jar")
    snooze(0.3)
    test.log("App Launch Successfully")