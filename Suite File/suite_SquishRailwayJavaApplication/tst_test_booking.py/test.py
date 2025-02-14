import json
import names
source(findFile("scripts", "BookTicket.py"))
source(findFile("scripts", "CommonFunctions.py"))


def main():
    # Load test data from JSON file
    json_file_path = r"C:\Users\SpanIdea\OneDrive\Desktop\Squish Automation\Scripts\DataFile\BookTicket.json"
    
    with open(json_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)   
    
    # Loop through the tickets data
    def test_booking_submit():
        
        for ticket in data["BookTicket"]:
            
            # Execute actions
            launch_application()  
            fill_booking_form(ticket)
    
    def test_cancle_button():    
        for ticket1 in data["CancleButton"]:
            
            # Execute actions
            launch_application()  
            Cancle_button_Working(ticket1)  
    
    test_booking_submit()
    test_cancle_button()
            

         