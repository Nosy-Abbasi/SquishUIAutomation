# -*- coding: utf-8 -*-  
import json
from squish import *
import sys
import os

import names
import BookingTicketLocators


def fill_booking_form(data):
    # Fill out the booking form with data
    Click(BookingTicketLocators.book_Tickets,"Booking button")
    
    Enter_Text(BookingTicketLocators.Full_Name,data["Full Name"])
    
    Enter_Text(BookingTicketLocators.Email_Id,data["Email"])
    
    Click(BookingTicketLocators.Day_RadioButton," Radio button - Shift - Day")
    
    Enter_Text(BookingTicketLocators.Time,data["Time"])
    
    Enter_Text(BookingTicketLocators.Train_Name,data["Train Name"])
    
    Enter_Text(BookingTicketLocators.Starting_From,data["Starting From"])
    
    Enter_Text(BookingTicketLocators.Destination,data["Destination"])
    
    Click(BookingTicketLocators.Add_Button,"Add button")
    
    Click(BookingTicketLocators.Yes_Button,"Yes button")
    
    Text_Verification(BookingTicketLocators.message_Ticket_is_booked_sucessfully,data["Expected Message"])


def Cancle_button_Working(data):
    
    Click(BookingTicketLocators.book_Tickets,"Booking button")
    
    Enter_Text(BookingTicketLocators.Full_Name,data["Full Name"])
    
    Enter_Text(BookingTicketLocators.Email_Id,data["Email"])
    
    Click(BookingTicketLocators.Day_RadioButton," Radio button - Shift - Day")
    
    Enter_Text(BookingTicketLocators.Time,data["Time"])
    
    Enter_Text(BookingTicketLocators.Train_Name,data["Train Name"])
    
    Enter_Text(BookingTicketLocators.Starting_From,data["Starting From"])
    
    Enter_Text(BookingTicketLocators.Destination,data["Destination"])
    
    Click(BookingTicketLocators.Add_Button,"Add button")
    
    Click(BookingTicketLocators.No_Button,"No button")
    
    test.passes("Test Passed")
    
        

