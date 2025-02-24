import json
import names
source(findFile("scripts", "Login.py"))
source(findFile("scripts", "CommonFunctions.py"))
source(findFile("scripts", "GVariables.py"))

def main():
    
    data = data_load(LoginJSON)
    
    def test_login():

        for ticket in data["Login"]:

            launch_application(Railway)  
            LoginFunctionlity(ticket)
            Close_Application(Railway)
     
    test_login()