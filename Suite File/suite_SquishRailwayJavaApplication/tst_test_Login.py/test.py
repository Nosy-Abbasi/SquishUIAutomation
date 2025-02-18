import json
import names
source(findFile("scripts", "Login.py"))
source(findFile("scripts", "CommonFunctions.py"))
source(findFile("scripts", "GVariables.py"))

def main():
    
    data = data_load(LoginJSON)
    
    def test_login():
    # Loop through the tickets data
        for ticket in data["Login"]:
            
            # Execute actions
            launch_application(Railway)  
            LoginFunctionlity(ticket)
            
    #Calling Functions        
    test_login()