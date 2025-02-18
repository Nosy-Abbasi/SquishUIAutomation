# encoding: UTF-8

from objectmaphelper import *

o_UserLogin = {"caption": "", "type": "User.UserLogin", "visible": True}
book_Tickets = {"caption": "Book Tickets", "type": "javax.swing.JButton", "visible": True, "window": o_UserLogin}
booking_Panel_Add = {"caption": "Booking Panel", "type": "Admin.Add", "visible": True}
booking_Panel_Full_Name_JLabel = {"caption": "Full Name", "type": "javax.swing.JLabel", "visible": True, "window": booking_Panel_Add}
Full_Name = {"leftWidget": booking_Panel_Full_Name_JLabel, "type": "javax.swing.JTextArea", "visible": True, "window": booking_Panel_Add}
booking_Panel_Email_Id_JLabel = {"caption": "Email Id", "type": "javax.swing.JLabel", "visible": True, "window": booking_Panel_Add}
Email_Id = {"leftWidget": booking_Panel_Email_Id_JLabel, "type": "javax.swing.JTextArea", "visible": True, "window": booking_Panel_Add}
Day_RadioButton = {"caption": "Day", "type": "javax.swing.JRadioButton", "visible": True, "window": booking_Panel_Add}
booking_Panel_Time_JLabel = {"caption": "Time", "type": "javax.swing.JLabel", "visible": True, "window": booking_Panel_Add}
Time = {"leftWidget": booking_Panel_Time_JLabel, "type": "javax.swing.JTextArea", "visible": True, "window": booking_Panel_Add}
booking_Panel_Train_Name_JLabel = {"caption": "Train Name", "type": "javax.swing.JLabel", "visible": True, "window": booking_Panel_Add}
Train_Name = {"leftWidget": booking_Panel_Train_Name_JLabel, "type": "javax.swing.JTextArea", "visible": True, "window": booking_Panel_Add}
booking_Panel_Starting_From_JLabel = {"caption": "Starting From", "type": "javax.swing.JLabel", "visible": True, "window": booking_Panel_Add}
Starting_From = {"leftWidget": booking_Panel_Starting_From_JLabel, "type": "javax.swing.JTextArea", "visible": True, "window": booking_Panel_Add}
booking_Panel_Destination_JLabel = {"caption": "Destination", "type": "javax.swing.JLabel", "visible": True, "window": booking_Panel_Add}
Destination = {"leftWidget": booking_Panel_Destination_JLabel, "type": "javax.swing.JTextArea", "visible": True, "window": booking_Panel_Add}
Add_Button = {"caption": "Add", "type": "javax.swing.JButton", "visible": True, "window": booking_Panel_Add}
select_an_Option_JDialog = {"caption": "Select an Option", "type": "javax.swing.JDialog", "visible": True}
Yes_Button = {"caption": "Yes", "name": "OptionPane.button", "type": "javax.swing.JButton", "visible": True, "window": select_an_Option_JDialog}
message_JDialog = {"caption": "Message", "type": "javax.swing.JDialog", "visible": True}
message_OK_JButton = {"caption": "OK", "name": "OptionPane.button", "type": "javax.swing.JButton", "visible": True, "window": message_JDialog}
message_Ticket_is_booked_sucessfully = {"caption": "Ticket is booked sucessfully.", "name": "OptionPane.label", "type": "javax.swing.JLabel", "visible": True, "window": message_JDialog}
No_Button = {"caption": "No", "name": "OptionPane.button", "type": "javax.swing.JButton", "visible": True, "window": select_an_Option_JDialog}
booking_Panel_Add = {"caption": "Booking Panel", "type": "Admin.Add", "visible": True}
booking_Panel_DD_MM_YYYY_JLabel = {"caption": "DD/MM/YYYY", "type": "javax.swing.JLabel", "visible": True, "window": booking_Panel_Add}
DD_ComboBox = {"caption": "", "leftWidget": booking_Panel_DD_MM_YYYY_JLabel, "type": "javax.swing.plaf.metal.MetalComboBoxButton", "visible": True, "window": booking_Panel_Add}
booking_Panel_ComboBox_list_JList = {"basetype": "javax.swing.JList", "name": "ComboBox.list", "visible": True, "window": booking_Panel_Add}
list_12_ListItem = {"caption": 12, "container": booking_Panel_ComboBox_list_JList, "type": "com.froglogic.squish.awt.ListItemProxy"}

