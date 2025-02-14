import json
import names
source(findFile("scripts", "Login.py"))
source(findFile("scripts", "CommonFunctions.py"))


def main():
    # Load test data from JSON file
    json_file_path = r"C:\Users\SpanIdea\OneDrive\Desktop\Squish Automation\Scripts\DataFile\LoginData.json"
    
    with open(json_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    def test_login():
    # Loop through the tickets data
        for ticket in data["Login"]:
            
            # Execute actions
            launch_application()  
            LoginFunctionlity(ticket)
            
    #Calling Functions        
    test_login()