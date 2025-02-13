import json
import names
source(findFile("scripts", "BookTicket.py"))
source(findFile("scripts", "CommonFunctions.py"))
# source(findFile("Global Scripts","BookTicket.py"))
# source(findFile("Global Scripts","CommonFunctions.py"))


def main():
    # Load test data from JSON file
    json_file_path = r"C:\Users\SpanIdea\OneDrive\Desktop\Squish Automation\Scripts\DataFile\BookTicket.json"
    
    with open(json_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    # Loop through the tickets data
    for ticket in data["BookTicket"]:
        Expected_Message = ticket["Expected Message"]
        
        # Execute actions
        launch_application()  
        fill_booking_form(ticket)  
        verify_booking(Expected_Message)  