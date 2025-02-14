import json
import names

source(findFile("scripts", "BookTicket.py"))
source(findFile("scripts", "CommonFunctions.py"))
source(findFile("scripts", "GVariables.py"))


def main():
    # Load test data from JSON file
    json_file_path = BookTicketJSON
    
    with open(json_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)   
    
    # Loop through the tickets data
    def test_booking_submit():
        
        for ticket in data["BookTicket"]:
            
            # Execute actions
            launch_application(Railway)  
            fill_booking_form(ticket)
    
    def test_cancle_button():    
        for ticket1 in data["CancleButton"]:
            
            # Execute actions
            launch_application(Railway)  
            Cancle_button_Working(ticket1)  
    
    test_booking_submit()
    test_cancle_button()
            

         