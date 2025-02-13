# -*- coding: utf-8 -*-  
import json
from squish import *
import sys
import os

import names

def launch_application():
    # Start the application
    startApplication("railway.jar")
    snooze(0.3)
    test.log("App Launch Successfully")