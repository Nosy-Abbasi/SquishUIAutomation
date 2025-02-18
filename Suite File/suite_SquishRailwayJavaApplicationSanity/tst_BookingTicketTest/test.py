import json
import names

source(findFile("scripts", "BookTicket.py"))
source(findFile("scripts", "CommonFunctions.py"))
source(findFile("scripts", "GVariables.py"))


def main():
    
    data = data_load(BookTicketJSON)
    

    def test_booking_submit():
        
        for ticket in data["BookTicket"]:
            
            # Execute actions
            launch_application(Railway)  
            fill_booking_form(ticket)
            Save_Booking(ticket)
    
    test_booking_submit()
            

         