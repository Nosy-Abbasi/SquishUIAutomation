# -*- coding: utf-8 -*-  
import json
from squish import *
import sys
import os

source(findFile("scripts", "BookingTicketLocator.py"))


def fill_booking_form(data):
    # Fill out the booking form with data
    Click(book_Tickets,"Booking button")
    
    Enter_Text(Full_Name,data["Full Name"])
    
    Enter_Text(Email_Id,data["Email"])
    
    Click(Day_RadioButton," Radio button - Shift - Day")
    
    Enter_Text(Time,data["Time"])
    
    Enter_Text(Train_Name,data["Train Name"])
    
    Enter_Text(Starting_From,data["Starting From"])
    
    Enter_Text(Destination,data["Destination"])
    
    
def Save_Booking(data):
    
    Click(Add_Button,"Add button")
    
    Click(Yes_Button,"Yes button")
    
    Text_Verification(message_Ticket_is_booked_sucessfully,data["Expected Message"])


def Cancel_button_Working():
    
    Click(Add_Button,"Add button")
    
    Click(No_Button,"No button")
    
    test.passes("Test Passed")
    
        

