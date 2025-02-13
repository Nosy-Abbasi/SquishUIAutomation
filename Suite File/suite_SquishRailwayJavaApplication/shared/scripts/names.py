# encoding: UTF-8

from objectmaphelper import *

o_UserLogin = {"caption": "", "type": "User.UserLogin", "visible": True}
book_Tickets_JButton = {"caption": "Book Tickets", "type": "javax.swing.JButton", "visible": True, "window": o_UserLogin}
booking_Panel_Add = {"caption": "Booking Panel", "type": "Admin.Add", "visible": True}
booking_Panel_Full_Name_JLabel = {"caption": "Full Name", "type": "javax.swing.JLabel", "visible": True, "window": booking_Panel_Add}
booking_Panel_Full_Name_JTextArea = {"leftWidget": booking_Panel_Full_Name_JLabel, "type": "javax.swing.JTextArea", "visible": True, "window": booking_Panel_Add}
booking_Panel_Email_Id_JLabel = {"caption": "Email Id", "type": "javax.swing.JLabel", "visible": True, "window": booking_Panel_Add}
booking_Panel_Email_Id_JTextArea = {"leftWidget": booking_Panel_Email_Id_JLabel, "type": "javax.swing.JTextArea", "visible": True, "window": booking_Panel_Add}
booking_Panel_Day_JRadioButton = {"caption": "Day", "type": "javax.swing.JRadioButton", "visible": True, "window": booking_Panel_Add}
booking_Panel_Time_JLabel = {"caption": "Time", "type": "javax.swing.JLabel", "visible": True, "window": booking_Panel_Add}
booking_Panel_Time_JTextArea = {"leftWidget": booking_Panel_Time_JLabel, "type": "javax.swing.JTextArea", "visible": True, "window": booking_Panel_Add}
booking_Panel_Train_Name_JLabel = {"caption": "Train Name", "type": "javax.swing.JLabel", "visible": True, "window": booking_Panel_Add}
booking_Panel_Train_Name_JTextArea = {"leftWidget": booking_Panel_Train_Name_JLabel, "type": "javax.swing.JTextArea", "visible": True, "window": booking_Panel_Add}
booking_Panel_Starting_From_JLabel = {"caption": "Starting From", "type": "javax.swing.JLabel", "visible": True, "window": booking_Panel_Add}
booking_Panel_Starting_From_JTextArea = {"leftWidget": booking_Panel_Starting_From_JLabel, "type": "javax.swing.JTextArea", "visible": True, "window": booking_Panel_Add}
booking_Panel_Destination_JLabel = {"caption": "Destination", "type": "javax.swing.JLabel", "visible": True, "window": booking_Panel_Add}
booking_Panel_Destination_JTextArea = {"leftWidget": booking_Panel_Destination_JLabel, "type": "javax.swing.JTextArea", "visible": True, "window": booking_Panel_Add}
booking_Panel_Add_JButton = {"caption": "Add", "type": "javax.swing.JButton", "visible": True, "window": booking_Panel_Add}
select_an_Option_JDialog = {"caption": "Select an Option", "type": "javax.swing.JDialog", "visible": True}
select_an_Option_Yes_JButton = {"caption": "Yes", "name": "OptionPane.button", "type": "javax.swing.JButton", "visible": True, "window": select_an_Option_JDialog}
message_JDialog = {"caption": "Message", "type": "javax.swing.JDialog", "visible": True}
message_OK_JButton = {"caption": "OK", "name": "OptionPane.button", "type": "javax.swing.JButton", "visible": True, "window": message_JDialog}
message_Ticket_is_booked_sucessfully_JLabel = {"caption": "Ticket is booked sucessfully.", "name": "OptionPane.label", "type": "javax.swing.JLabel", "visible": True, "window": message_JDialog}
select_an_Option_No_JButton = {"caption": "No", "name": "OptionPane.button", "type": "javax.swing.JButton", "visible": True, "window": select_an_Option_JDialog}
admin_Login_JButton = {"caption": "Admin Login", "type": "javax.swing.JButton", "visible": True, "window": o_UserLogin}
admin_Login_AdminLogin = {"caption": "Admin Login", "type": "Admin.AdminLogin", "visible": True}
admin_Login_Admin_ID_JLabel = {"caption": "Admin-ID", "type": "javax.swing.JLabel", "visible": True, "window": admin_Login_AdminLogin}
admin_Login_Admin_ID_JTextField = {"leftWidget": admin_Login_Admin_ID_JLabel, "type": "javax.swing.JTextField", "visible": True, "window": admin_Login_AdminLogin}
admin_Login_Password_JLabel = {"caption": "Password", "type": "javax.swing.JLabel", "visible": True, "window": admin_Login_AdminLogin}
admin_Login_Password_JPasswordField = {"leftWidget": admin_Login_Password_JLabel, "type": "javax.swing.JPasswordField", "visible": True, "window": admin_Login_AdminLogin}
admin_Login_Login_JButton = {"caption": "Login", "type": "javax.swing.JButton", "visible": True, "window": admin_Login_AdminLogin}
message_Wrong_Username_Password_JLabel = {"caption": "Wrong Username & Password", "name": "OptionPane.label", "type": "javax.swing.JLabel", "visible": True, "window": message_JDialog}
