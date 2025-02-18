# encoding: UTF-8

from objectmaphelper import *

o_UserLogin = {"caption": "", "type": "User.UserLogin", "visible": True}
admin_Login = {"caption": "Admin Login", "type": "javax.swing.JButton", "visible": True, "window": o_UserLogin}
admin_Login_AdminLogin = {"caption": "Admin Login", "type": "Admin.AdminLogin", "visible": True}
admin_Login_Admin_ID_JLabel = {"caption": "Admin-ID", "type": "javax.swing.JLabel", "visible": True, "window": admin_Login_AdminLogin}
Admin_ID = {"leftWidget": admin_Login_Admin_ID_JLabel, "type": "javax.swing.JTextField", "visible": True, "window": admin_Login_AdminLogin}
admin_Login_Password_JLabel = {"caption": "Password", "type": "javax.swing.JLabel", "visible": True, "window": admin_Login_AdminLogin}
Password = {"leftWidget": admin_Login_Password_JLabel, "type": "javax.swing.JPasswordField", "visible": True, "window": admin_Login_AdminLogin}
Login = {"caption": "Login", "type": "javax.swing.JButton", "visible": True, "window": admin_Login_AdminLogin}
message_JDialog = {"caption": "Message", "type": "javax.swing.JDialog", "visible": True}
Wrong_Username_Password = {"caption": "Wrong Username & Password", "name": "OptionPane.label", "type": "javax.swing.JLabel", "visible": True, "window": message_JDialog}
