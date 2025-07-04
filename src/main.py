from PyQt6 import QtWidgets, uic, QtCore, QtGui
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem, QInputDialog
from PyQt6.QtCore import QTimer
import mysql.connector

from helpers.DatabaseHelper import DatabaseHelper
from helpers.UIHelper import UIHelper
from helpers.GraphHelper import GraphHelper
from ui.AdminPanel import Ui_AdminPanel
from ui.Login import Ui_LoginPage
from ui.MainPage import Ui_MainPage
from ui.Register import Ui_RegisterPage
from resources.images.ui_rc import *
import bcrypt # type: ignore
import re
from dotenv import load_dotenv # type: ignore
from prophet_model import predict_next_day_usage
import os

def create_connection():
    load_dotenv()
    print("[DEBUG] Starting database connection...")
    try:
        #database is hosted locally use the below creds
        host = os.getenv('db_host_local')
        user = os.getenv('db_user_local')
        password = os.getenv('db_password_local')
        database = os.getenv('db_name_local')

        #port is same for both local and online
        port = os.getenv('db_port')

        #database is hosted online use the below creds
        host_online = os.getenv('db_host_online')
        user_online = os.getenv('db_user_online')
        password_online = os.getenv('db_password_online')
        database_online = os.getenv('db_name_online')

        print(f"[DEBUG] Attempting to connect to database with hardcoded credentials:")
        print(f"[DEBUG] Host: localhost")
        print(f"[DEBUG] User: root")
        print(f"[DEBUG] Database: energy")
        print(f"[DEBUG] Port: 3306")

        db = mysql.connector.connect(
            host= "localhost",
            user="root",
            password="delllatitude7480",
            database="energy",
            port  = 3306
        )
        print("[DEBUG] Database connection established successfully.")
        return db
    except mysql.connector.Error as err:
        print(f"[ERROR] Database connection failed: {err}")
        return None
    except Exception as e:
        print(f"[ERROR] Unexpected error during database connection: {e}")
        return None

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_LoginPage()
        self.ui.setupUi(self)
        self.ui.btnLogin.clicked.connect(self.handle_login)
        self.ui.btnRegister.clicked.connect(self.open_register)
        self.db_helper = DatabaseHelper(create_connection())
        self.ui.inputUsername.returnPressed.connect(self.handle_login)
        self.ui.inputPassword.returnPressed.connect(self.handle_login)

    # def handle_login(self):
    #         username = self.ui.inputUsername.text()
    #         password = self.ui.inputPassword.text()

    #         if not username or not password:
    #             UIHelper.show_message(self, 'warning', 'Error', 'All fields must be filled in.')
    #             return

    #         # First, get the stored hashed password for this username
    #         result = self.db_helper.fetch_one("SELECT * FROM users WHERE Username = %s", (username,))

    #         if result:
    #             stored_password = result[4]  # Assuming Password is at index 3 in your users table
                
    #             # Check if the provided password matches the stored hash
    #             if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
    #                 self.close()
    #                 user_type = result[-1]  # Get the UserType of the user
                    
    #                 if user_type == 0:  # Normal user
    #                     self.main = Main(username, self.db_helper.db)
    #                     self.main.show()
    #                 elif user_type == 1:  # Admin user
    #                     reply = UIHelper.show_message(self, 'question', 'Admin Panel', 
    #                                             'Do you want to open the admin panel?')
    #                     if reply == QtWidgets.QMessageBox.StandardButton.Yes:
    #                         self.admin = AdminPanel(username, self.db_helper.db)
    #                         self.admin.show()
    #                     else:
    #                         self.main = Main(username, self.db_helper.db)
    #                         self.main.show()
    #             else:
    #                 UIHelper.show_message(self, 'warning', 'Error', 'Wrong username or password.')
    #         else:
    #             UIHelper.show_message(self, 'warning', 'Error', 'Wrong username or password.')


    def handle_login(self):
        username = self.ui.inputUsername.text()
        password = self.ui.inputPassword.text()

        if not username or not password:
            UIHelper.show_message(self, 'warning', 'Error', 'All fields must be filled in.')
            return

        # Fetch user details
        result = self.db_helper.fetch_one("SELECT * FROM users WHERE Username = %s", (username,))

        if result:
            stored_password = result[4]  # Assuming Password is at index 4
            user_id = result[0]  # Assuming User ID is at index 0

            # Check if the password is hashed (bcrypt hashes start with "$2b$")
            if not stored_password.startswith("$2b$"):
                print(f"[DEBUG] Plaintext password detected for user {username}: {stored_password}")

                # Convert plaintext password to bcrypt hash
                hashed_password = bcrypt.hashpw(stored_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

                print(f"[DEBUG] New hashed password: {hashed_password}")

                # Update database with the newly hashed password
                update_success = self.db_helper.execute_query(
                    "UPDATE users SET Password = %s WHERE ID = %s",
                    (hashed_password, user_id)
                )

                if update_success:
                    print("[DEBUG] Password successfully updated in database!")
                    self.db_helper.db.commit()  # Ensure changes are committed
                else:
                    print("[ERROR] Failed to update password in database.")

                # Use the newly hashed password for authentication
                stored_password = hashed_password

            # Verify password (now stored_password is guaranteed to be hashed)
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                self.close()
                user_type = result[-1]  # Get the UserType of the user
                
                if user_type == 0:  # Normal user
                    self.main = Main(username, self.db_helper.db)
                    self.main.show()
                elif user_type == 1:  # Admin user
                    reply = UIHelper.show_message(self, 'question', 'Admin Panel', 
                                            'Do you want to open the admin panel?')
                    if reply == QtWidgets.QMessageBox.StandardButton.Yes:
                        self.admin = AdminPanel(username, self.db_helper.db)
                        self.admin.show()
                    else:
                        self.main = Main(username, self.db_helper.db)
                        self.main.show()
            else:
                UIHelper.show_message(self, 'warning', 'Error', 'Wrong username or password.')
        else:
            UIHelper.show_message(self, 'warning', 'Error', 'Wrong username or password.')


    def open_register(self):
        self.register = Register(self.db_helper.db)
        self.register.show()

class Register(QtWidgets.QMainWindow):
    def __init__(self, db):
        super(Register, self).__init__()
        self.ui = Ui_RegisterPage()
        self.ui.setupUi(self)
        self.ui.btnRegister.clicked.connect(self.handle_register)
        self.db_helper = DatabaseHelper(db)
        self.ui.inputName.returnPressed.connect(self.handle_register)
        self.ui.inputSurname.returnPressed.connect(self.handle_register)
        self.ui.inputUsername.returnPressed.connect(self.handle_register)
        self.ui.inputPassword.returnPressed.connect(self.handle_register)
        self.ui.inputEmail.returnPressed.connect(self.handle_register)
        self.ui.inputPhone.returnPressed.connect(self.handle_register)
        self.ui.inputStreet.returnPressed.connect(self.handle_register)
        self.ui.inputCity.returnPressed.connect(self.handle_register)
        self.ui.inputState.returnPressed.connect(self.handle_register)
        self.ui.inputPincode.returnPressed.connect(self.handle_register)

    def validate_email(self, email):
        """Returns True if email is valid, False otherwise."""
        if not email:
            return False

        try:
            # Check for @ symbol
            if '@' not in email:
                return False
            
            # Split email into local and domain parts
            local, domain = email.rsplit('@', 1)
            
            # Check for minimum lengths
            if not local or not domain:
                return False
                
            # Check for domain has at least one period
            if '.' not in domain:
                return False
                
            # Check domain ends properly
            domain_parts = domain.split('.')
            if len(domain_parts[-1]) < 2:  # Last part should be at least 2 chars
                return False
                
            return True
            
        except Exception:
            return False
        
    def validate_phone(self, phone):
        """Returns True if phone number is valid (10 digits), False otherwise."""
        if not phone:
            return False
        
        # Check if it's exactly 10 digits
        return phone.isdigit() and len(phone) == 10
    
    def validate_registration_button(self):
        """Enable/disable register button based on email and phone validity."""
        email = self.ui.inputEmail.text()
        phone = self.ui.inputPhone.text()
        is_valid = self.validate_email(email) and self.validate_phone(phone)
        self.ui.btnRegister.setEnabled(is_valid)

    def validate_password(self, password):
        """
        Ensures the password is:
        - At least 8 characters long
        - Contains at least one special character
        - Contains at least one number
        """
        if len(password) < 8:
            return False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False
        if not re.search(r"\d", password):
            return False
        return True

    def handle_register(self):
        name = self.ui.inputName.text()
        surname = self.ui.inputSurname.text()
        username = self.ui.inputUsername.text()
        password = self.ui.inputPassword.text()
        email = self.ui.inputEmail.text()
        phone = self.ui.inputPhone.text()
        street = self.ui.inputStreet.text()
        city = self.ui.inputCity.text()
        state = self.ui.inputState.text()
        pincode = self.ui.inputPincode.text()

        if not name or not surname or not username or not password or not email or not phone or not street or not city or not state or not pincode:
            UIHelper.show_message(self, 'warning', 'Error', 'All fields must be filled in.')
            return
            
        if not self.validate_email(email):
            UIHelper.show_message(self, 'warning', 'Error', 'Please enter a valid email address.')
            return
            
        if not self.validate_phone(phone):
            UIHelper.show_message(self, 'warning', 'Error', 'Please enter a valid 10-digit phone number.')
            return
        
        if not self.validate_password(password):
            UIHelper.show_message(self, 'warning', 'Error', 'Password must be at least 8 characters long, contain at least one special character, and one number.')
            return

        result = self.db_helper.fetch_one("SELECT * FROM users WHERE UserName = %s", (username,))
        if result:
            UIHelper.show_message(self, 'warning', 'Error', 'This username is already taken.')
            return

        # Hash the password
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        # Store the hashed password in the database
        self.db_helper.insert(
            "INSERT INTO users (Fname, Lname, Username, Password, Street, City, State, Pincode, Phoneno, Email) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (name, surname, username, hashed_password, street, city, state, pincode, phone, email)
        )
        
        UIHelper.show_message(self, 'info', 'Success', 'Registered successfully. You can log in now.')
        self.close()

class Main(QtWidgets.QMainWindow):
    def __init__(self, username, db):
        super(Main, self).__init__()
        self.ui = Ui_MainPage()
        self.ui.setupUi(self)
        self.username = username
        self.db = db
        self.setup_connections()
        self.db_helper = DatabaseHelper(db)
        self.userID = self.get_user_id()
        self.load_user_info()
        self.load_registered_meters()
        self.load_connected_devices()
        self.load_available_devices()
        self.load_consumption_records()
        self.load_consumption_analytics()
        self.resize_timer = QTimer()
        self.resize_timer.setSingleShot(True)
        self.resize_timer.timeout.connect(self.redraw_graphs)
        self.load_energy_insights()
        self.load_billing_details()

    def resizeEvent(self, event):
        # Start or restart the timer whenever the window is resized
        self.resize_timer.start(100)  # 500 ms delay

    def redraw_graphs(self):
        # Redraw the graphs
        self.draw_daily_device_usage()
        self.draw_historical_device_usage()
        self.draw_daily_energy_overview()
        self.draw_monthly_energy_overview()
        self.draw_daily_bill_summary()
        self.draw_monthly_bill_summary()
        
    def tab_changed(self, index):
        # Check if the tabConsumptionAnalytics tab is selected
        if self.ui.tabWidget.widget(index) is self.ui.tabConsumptionAnalytics:
            # Redraw the graph
            self.draw_daily_device_usage()
            self.draw_historical_device_usage()
        
        if self.ui.tabWidget.widget(index) is self.ui.tabEnergyInsights:
            # Redraw the graph
            self.draw_daily_energy_overview()
            self.draw_monthly_energy_overview()
            
        if self.ui.tabWidget.widget(index) is self.ui.tabBillingDetails:
            # Redraw the graph
            self.draw_daily_bill_summary()
            self.draw_monthly_bill_summary()
    
    def setup_connections(self):
        # Set bold font for the labels
        font = QtGui.QFont()
        font.setBold(True)
        self.ui.labelUserInformation.setFont(font)
        self.ui.labelSecuritySettings.setFont(font)
        self.ui.labelUpdatePassword.setFont(font)
        self.ui.labelUpdateUsername.setFont(font)
        self.ui.labelRemoveAccount.setFont(font)
        self.ui.labelRegisteredMeters.setFont(font)
        self.ui.labelAddMeter.setFont(font)
        self.ui.labelRemoveMeter.setFont(font)
        self.ui.labelConnectedDevices.setFont(font)
        self.ui.labelRegisterNewDevice.setFont(font)
        self.ui.labelAvailableDevices.setFont(font)
        self.ui.labelLogConsumption.setFont(font)
        self.ui.labelDeviceConsumptionAnalysis.setFont(font)
        self.ui.labelViewConsumptionHistory.setFont(font)
        self.ui.labelDailyDeviceUsage.setFont(font)
        self.ui.labelHistoricalDeviceUsage.setFont(font)
        self.ui.labelDailyEnergyOverview.setFont(font)
        self.ui.labelMonthlyEnergyOverview.setFont(font)
        self.ui.labelDailyBillSummary.setFont(font)
        self.ui.labelMonthlyBillSummary.setFont(font)

        # # Connect the logout button
        # self.ui.btnLogout.clicked.connect(self.handle_logout)

        # Connect the tabWidget signal
        self.ui.tabWidget.currentChanged.connect(self.tab_changed)

        # Connect the buttons to their respective handlers
        self.ui.btnUpdatePassword.clicked.connect(self.update_password)
        self.ui.btnUpdateUsername.clicked.connect(self.update_username)
        self.ui.btnRemoveAccount.clicked.connect(self.remove_account)
        self.ui.btnAddMeter_Add.clicked.connect(self.add_meter)
        self.ui.btnRemoveMeter_Remove.clicked.connect(self.remove_meter)
        self.ui.comboConnectedDevices_MeterID.currentIndexChanged.connect(self.load_connected_devices)
        self.ui.comboDailyDeviceUsage_Meter.currentIndexChanged.connect(self.update_daily_device_usage_date)
        self.ui.comboDailyDeviceUsage_Date.currentIndexChanged.connect(self.draw_daily_device_usage)
        self.ui.comboDailyDeviceUsage_GraphType.currentIndexChanged.connect(self.draw_daily_device_usage)
        self.ui.comboHistoricalDeviceUsage_Meter.currentIndexChanged.connect(self.draw_historical_device_usage)
        self.ui.comboHistoricalDeviceUsage_GraphType.currentIndexChanged.connect(self.draw_historical_device_usage)
        self.ui.comboDailyEnergyOverview_Meter.currentIndexChanged.connect(self.draw_daily_energy_overview)
        self.ui.comboDailyEnergyOverview_GraphType.currentIndexChanged.connect(self.draw_daily_energy_overview)
        self.ui.comboMonthlyEnergyOverview_Meter.currentIndexChanged.connect(self.draw_monthly_energy_overview)
        self.ui.comboMonthlyEnergyOverview_GraphType.currentIndexChanged.connect(self.draw_monthly_energy_overview)
        self.ui.comboDailyBillSummary_Meter.currentIndexChanged.connect(self.draw_daily_bill_summary)
        self.ui.comboDailyBillSummary_GraphType.currentIndexChanged.connect(self.draw_daily_bill_summary)
        self.ui.comboMonthlyBillSummary_Meter.currentIndexChanged.connect(self.draw_monthly_bill_summary)
        self.ui.comboMonthlyBillSummary_GraphType.currentIndexChanged.connect(self.draw_monthly_bill_summary)

        # Connect the returnPressed signals
        self.ui.inputUpdatePassword_CurrentPassword.returnPressed.connect(self.update_password)
        self.ui.inputUpdatePassword_NewPassword.returnPressed.connect(self.update_password)
        self.ui.inputUpdatePassword_ConfirmPassword.returnPressed.connect(self.update_password)
        self.ui.inputUpdateUsername_VerifyPassword.returnPressed.connect(self.update_username)
        self.ui.inputUpdateUsername_NewUsername.returnPressed.connect(self.update_username)
        self.ui.inputUpdateUsername_ConfirmUsername.returnPressed.connect(self.update_username)
        self.ui.inputRemoveAccount_VerifyPassword.returnPressed.connect(self.remove_account)
    
    def get_user_id(self):
        result = self.db_helper.fetch_one("SELECT ID FROM users WHERE UserName = %s", (self.username,))
        return result[0] if result else None
    
    def load_user_info(self):
        result = self.db_helper.fetch_one("SELECT * FROM users WHERE UserName = %s", (self.username,))
    
        if result:
            self.ui.labelHeader_FNameandLnameDynamic.setText(f"{result[1]} {result[2]}")
            self.ui.labelUserInfo_UidDynamic.setText(str(result[0]))
            self.ui.labelUserInfo_FnameDynamic.setText(result[1])
            self.ui.labelUserInfo_LnameDynamic.setText(result[2])
            self.ui.labelUserInfo_UsernameDynamic.setText(result[3])

    def update_password(self):
        current_password = self.ui.inputUpdatePassword_CurrentPassword.text()
        new_password = self.ui.inputUpdatePassword_NewPassword.text()
        confirm_password = self.ui.inputUpdatePassword_ConfirmPassword.text()

        result = self.db_helper.fetch_one("SELECT * FROM users WHERE UserName = %s AND Password = %s", (self.username, current_password))

        if not result:
            UIHelper.show_message(self, 'warning', 'Error', 'Current password is incorrect.')
            return

        if new_password != confirm_password:
            UIHelper.show_message(self, 'warning', 'Error', 'New password and confirm password do not match.')
            return

        self.db_helper.update("UPDATE users SET Password = %s WHERE UserName = %s", (new_password, self.username))
        UIHelper.show_message(self, 'info', 'Success', 'Password updated successfully.')

    def update_username(self):
        verify_password = self.ui.inputUpdateUsername_VerifyPassword.text()
        new_username = self.ui.inputUpdateUsername_NewUsername.text()
        confirm_username = self.ui.inputUpdateUsername_ConfirmUsername.text()

        result = self.db_helper.fetch_one("SELECT * FROM users WHERE UserName = %s AND Password = %s", (self.username, verify_password))

        if not result:
            UIHelper.show_message(self, 'warning', 'Error', 'Password is incorrect.')
            return

        if new_username != confirm_username:
            UIHelper.show_message(self, 'warning', 'Error', 'New username and confirm username do not match.')
            return

        result = self.db_helper.fetch_one("SELECT * FROM users WHERE UserName = %s", (new_username,))

        if result:
            UIHelper.show_message(self, 'warning', 'Error', 'This username is already taken.')
            return

        self.db_helper.update("UPDATE users SET UserName = %s WHERE UserName = %s", (new_username, self.username))
        UIHelper.show_message(self, 'info', 'Success', 'Username updated successfully.')
        self.username = new_username  # Update the current username
        self.load_user_info()

    def remove_account(self):
        verify_password = self.ui.inputRemoveAccount_VerifyPassword.text()
        
        result = self.db_helper.fetch_one("SELECT * FROM users WHERE UserName = %s AND Password = %s", (self.username, verify_password))
        if not result:
            UIHelper.show_message(self, 'warning', 'Error', 'Password is incorrect.')
            return
        
        self.db_helper.delete("DELETE FROM usersmeters WHERE UserID = %s", (self.userID,))
        self.db_helper.delete("DELETE FROM usages WHERE UserID = %s", (self.userID,))
        self.db_helper.delete("DELETE FROM usersdevices WHERE UserID = %s", (self.userID,))
        self.db_helper.delete("DELETE FROM users WHERE UserName = %s", (self.username,))
        UIHelper.show_message(self, 'info', 'Success', 'Account removed successfully.')
        self.close()  # Close the main window
    
    def load_registered_meters(self):
        query = """
            SELECT meter.meterID, meter.type, meter.location 
            FROM meter 
            INNER JOIN usersmeters ON meter.meterID = usersmeters.MeterID 
            WHERE usersmeters.UserID = %s
        """
        result = self.db_helper.fetch_all(query, (self.userID,))
        UIHelper.update_table(self.ui.tableRegisteredMeters, result)

    def add_meter(self):
        meter_type = self.ui.comboAddMeter_MeterType.currentText()
        location = self.ui.comboAddMeter_Location.currentText()
    
        meter_id = self.db_helper.insert("INSERT INTO meter (type, location) VALUES (%s, %s)", (meter_type, location))
        self.db_helper.insert("INSERT INTO usersmeters (UserID, MeterID) VALUES (%s, %s)", (self.userID, meter_id))
    
        UIHelper.show_message(self, 'info', "Success", "Meter added successfully.")
    
        self.load_registered_meters()
        self.load_connected_devices()
        self.update_user_meters()
    
    def remove_meter(self):        
        meter_id = self.ui.comboRemoveMeter_MeterID.currentText()
        
        result = self.db_helper.fetch_one("""
            SELECT meter.meterID 
            FROM meter 
            INNER JOIN usersmeters ON meter.meterID = usersmeters.MeterID 
            WHERE usersmeters.UserID = %s AND meter.meterID = %s
        """, (self.userID, meter_id))
    
        if result is None:
            UIHelper.show_message(self, 'warning', "Error", "No such meter found.")
            return
        
        # Confirmation dialog
        confirmation = UIHelper.show_message(self, 'question', "Confirmation", "Are you sure you want to remove this meter?")
        if confirmation == QMessageBox.StandardButton.Yes:
            self.db_helper.delete("DELETE FROM usersdevices WHERE UserID = %s AND MeterID = %s", (self.userID, meter_id))
            self.db_helper.delete("DELETE FROM usersmeters WHERE UserID = %s AND MeterID = %s", (self.userID, meter_id))
            self.db_helper.delete("DELETE FROM meter WHERE meterID = %s", (meter_id,))
            UIHelper.show_message(self, 'info', "Success", "Meter removed.")
            self.load_registered_meters()
            self.load_connected_devices()
            self.update_user_meters()
    
    def update_user_meters(self):
        meter_ids = [str(item[0]) for item in self.db_helper.fetch_all("""
            SELECT meter.meterID 
            FROM usersmeters 
            INNER JOIN meter ON usersmeters.MeterID = meter.meterID
            WHERE usersmeters.UserID = %s
        """, (self.userID,))]
            
        try:
            self.ui.comboConnectedDevices_MeterID.currentIndexChanged.disconnect()
            self.ui.comboRegisterNewDevice_AssociatedMeterID.currentIndexChanged.disconnect()
        except TypeError:
            pass
    
        UIHelper.update_combo_box(self.ui.comboRemoveMeter_MeterID, meter_ids)
        UIHelper.update_combo_box(self.ui.comboConnectedDevices_MeterID, meter_ids)
        UIHelper.update_combo_box(self.ui.comboRegisterNewDevice_AssociatedMeterID, meter_ids)
    
        UIHelper.update_combo_box(self.ui.comboLogConsumption_MeterID, meter_ids)
        UIHelper.update_combo_box(self.ui.comboViewConsumptionHistory_MeterID, meter_ids)
        UIHelper.update_combo_box(self.ui.comboDeviceConsumptionAnalysis_MeterID, meter_ids)

        UIHelper.update_combo_box(self.ui.comboDailyDeviceUsage_Meter, meter_ids)
        UIHelper.update_combo_box(self.ui.comboHistoricalDeviceUsage_Meter, meter_ids)

        UIHelper.update_combo_box(self.ui.comboDailyEnergyOverview_Meter, meter_ids)
        UIHelper.update_combo_box(self.ui.comboMonthlyEnergyOverview_Meter, meter_ids)
        
        UIHelper.update_combo_box(self.ui.comboDailyBillSummary_Meter, meter_ids)
        UIHelper.update_combo_box(self.ui.comboMonthlyBillSummary_Meter, meter_ids)

        self.ui.comboConnectedDevices_MeterID.currentIndexChanged.connect(lambda: self.load_connected_devices(False))
        self.ui.comboRegisterNewDevice_AssociatedMeterID.currentIndexChanged.connect(self.load_register_new_device)

        # Manually call load_register_new_device to populate the Device ID combo box
        self.load_register_new_device()

    def load_connected_devices(self, update_combo_box=True):
        if update_combo_box:
            self.update_user_meters()
            
        if self.ui.comboConnectedDevices_MeterID.count() == 0:
            return
    
        # Fetch the devices that are connected to the selected meter
        selected_meter_id = self.ui.comboConnectedDevices_MeterID.currentText()
        query = """
            SELECT usersdevices.DeviceID, devicedetails.DeviceName, devicedetails.Manufacturer, devicedetails.EnergyRating, devicedetails.`PowerConsumption (per Hour)`
            FROM usersdevices 
            INNER JOIN device ON usersdevices.DeviceID = device.DeviceID
            INNER JOIN devicedetails ON device.DeviceID = devicedetails.DeviceID
            WHERE usersdevices.UserID = %s AND usersdevices.MeterID = %s
        """
        cursor = self.db_helper.execute_query(query, (self.userID, selected_meter_id))

        # Populate the table with the fetched devices
        UIHelper.update_table(self.ui.tableConnectedDevices, cursor)
        
    def load_register_new_device(self):
        # Fetch all available device IDs
        query = "SELECT DeviceID FROM device"
        cursor = self.db_helper.execute_query(query)
        device_ids = [str(item[0]) for item in cursor.fetchall()]
    
        if self.ui.comboRegisterNewDevice_AssociatedMeterID.count() == 0:
            return
        
        # Clear the Device ID combo box and add the fetched device IDs
        UIHelper.update_combo_box(self.ui.comboRegisterNewDevice_DeviceID, device_ids)
    
        # Disconnect the clicked signal and connect the register_device_to_meter method to it
        try:
            self.ui.btnRegisterNewDevice.clicked.disconnect()
        except TypeError:
            pass  # Do nothing if the signal isn't connected to any slot
        self.ui.btnRegisterNewDevice.clicked.connect(self.register_device_to_meter)
    
    def register_device_to_meter(self):
        # Get the selected meter ID and device ID
        selected_meter_id = self.ui.comboRegisterNewDevice_AssociatedMeterID.currentText()
        selected_device_id = self.ui.comboRegisterNewDevice_DeviceID.currentText()
    
        # Check if the device is already associated with the user and meter
        query = """
            SELECT 1 
            FROM usersdevices 
            WHERE UserID = %s AND DeviceID = %s AND MeterID = %s
        """
        result = self.db_helper.fetch_one(query, (self.userID, selected_device_id, selected_meter_id))
        if result is not None:
            # The device is already associated with the user and meter, so show an error message and return
            UIHelper.show_message(self, 'error', "Error", "The device is already associated with the selected meter.")
            return
    
        # Add the selected device to the meter's connected devices
        query = """
            INSERT INTO usersdevices (UserID, DeviceID, MeterID)
            VALUES (%s, %s, %s)
        """
        self.db_helper.insert(query, (self.userID, selected_device_id, selected_meter_id))
    
        # Update the connected devices table
        self.load_connected_devices(True)
    
    def load_available_devices(self):
        # Fetch all available devices
        query = """
            SELECT device.DeviceID, devicedetails.DeviceName, devicedetails.Manufacturer, devicedetails.EnergyRating, devicedetails.`PowerConsumption (per Hour)`
            FROM device 
            INNER JOIN devicedetails ON device.DeviceID = devicedetails.DeviceID
            ORDER BY devicedetails.Manufacturer, devicedetails.DeviceName ASC
        """
        result = self.db_helper.execute_query(query)
    
        # Populate the table with the fetched devices
        UIHelper.update_table(self.ui.tableAvailableDevices, result)

    def load_consumption_records(self):
        self.ui.btnLogConsumption.clicked.connect(self.log_consumption)
        self.ui.comboViewConsumptionHistory_MeterID.currentIndexChanged.connect(lambda: self.update_date_combo_box(self.ui.comboViewConsumptionHistory_MeterID, self.ui.comboViewConsumptionHistory_Date))
        self.ui.comboViewConsumptionHistory_Date.currentIndexChanged.connect(self.view_consumption_history)
        self.ui.comboLogConsumption_MeterID.currentIndexChanged.connect(self.update_device_combo_box)
        self.ui.comboDeviceConsumptionAnalysis_MeterID.currentIndexChanged.connect(self.update_device_combo_box)
        self.ui.comboDeviceConsumptionAnalysis_DeviceID.currentIndexChanged.connect(self.device_consumption_analysis)
    
        # Auto-fill the View Consumption History and the graph of Device Consumption Analysis
        self.update_date_combo_box(self.ui.comboViewConsumptionHistory_MeterID, self.ui.comboViewConsumptionHistory_Date)
        self.update_device_combo_box()
        self.view_consumption_history()
        self.device_consumption_analysis()

    def update_device_combo_box(self):
        selected_meter_id_log = self.ui.comboLogConsumption_MeterID.currentText()
        selected_meter_id_analysis = self.ui.comboDeviceConsumptionAnalysis_MeterID.currentText()

        # Fetch all devices for the log consumption combo box
        query_log = """
        SELECT DISTINCT DeviceID 
        FROM usersdevices 
        WHERE UserID = %s AND MeterID = %s
        ORDER BY DeviceID
        """
        device_ids_log = [
            str(item[0]) 
            for item in self.db_helper.fetch_all(query_log, (self.userID, selected_meter_id_log))
        ]

        # Fetch devices with usage records for the device consumption analysis combo box
        query_analysis = """
        SELECT DISTINCT DeviceID 
        FROM usersdevices 
        WHERE UserID = %s AND MeterID = %s AND DeviceID IN (
            SELECT DISTINCT deviceID 
            FROM usages 
            WHERE userID = %s AND meterID = %s
        ) 
        ORDER BY DeviceID
        """
        device_ids_analysis = [
            str(item[0]) 
            for item in self.db_helper.fetch_all(query_analysis, (self.userID, selected_meter_id_analysis, self.userID, selected_meter_id_analysis))
        ]

        UIHelper.update_combo_box(self.ui.comboLogConsumption_DeviceID, device_ids_log)
        UIHelper.update_combo_box(self.ui.comboDeviceConsumptionAnalysis_DeviceID, device_ids_analysis)
    
    def update_date_combo_box(self, meter_combo_box, date_combo_box):
        selected_meter_id = meter_combo_box.currentText()

        query = "SELECT DISTINCT date FROM usages WHERE userID = %s AND meterID = %s ORDER BY date"
        dates = [str(item[0]) for item in self.db_helper.fetch_all(query, (self.userID, selected_meter_id))]

        UIHelper.update_combo_box(date_combo_box, dates)

    def log_consumption(self):
        selected_meter_id = self.ui.comboLogConsumption_MeterID.currentText()
        selected_device_id = self.ui.comboLogConsumption_DeviceID.currentText()
        date_of_usage = self.ui.dateLogConsumption_DateOfUsage.date().toPyDate()
        formatted_date = date_of_usage.strftime('%Y-%m-%d')
        consumption_duration = self.ui.doubleSpinBoxLogConsumption_ConsumptionDuration.value()
    
        # Check if a record with the same userID, deviceID, meterID, and date already exists
        query = "SELECT * FROM usages WHERE userID = %s AND deviceID = %s AND meterID = %s AND date = %s"
        existing_record = self.db_helper.fetch_one(query, (self.userID, selected_device_id, selected_meter_id, formatted_date))
    
        if existing_record:
            # If a record exists, update it
            query = "UPDATE usages SET usageAmount = %s WHERE userID = %s AND deviceID = %s AND meterID = %s AND date = %s"
            self.db_helper.execute_query(query, (consumption_duration, self.userID, selected_device_id, selected_meter_id, formatted_date))
        else:
            # If no record exists, insert a new one
            query = "INSERT INTO usages (userID, deviceID, meterID, date, usageAmount) VALUES (%s, %s, %s, %s, %s)"
            self.db_helper.insert(query, (self.userID, selected_device_id, selected_meter_id, formatted_date, consumption_duration))
    
        self.view_consumption_history()
        self.device_consumption_analysis()
        self.update_device_combo_box()
        self.update_date_combo_box(self.ui.comboViewConsumptionHistory_MeterID, self.ui.comboViewConsumptionHistory_Date)
        self.update_date_combo_box(self.ui.comboDailyDeviceUsage_Meter, self.ui.comboDailyDeviceUsage_Date)
        
    def view_consumption_history(self):
        selected_meter_id = self.ui.comboViewConsumptionHistory_MeterID.currentText()
        selected_date = self.ui.comboViewConsumptionHistory_Date.currentText()
        if selected_date:
            query = "SELECT deviceID, usageAmount FROM usages WHERE userID = %s AND meterID = %s AND date = %s"
            data = self.db_helper.fetch_all(query, (self.userID, selected_meter_id, selected_date))

            UIHelper.update_table(self.ui.tableViewConsumptionHistory, data)

    def device_consumption_analysis(self):
        selected_meter_id = self.ui.comboDeviceConsumptionAnalysis_MeterID.currentText()
        selected_device_id = self.ui.comboDeviceConsumptionAnalysis_DeviceID.currentText()

        query = "SELECT date, usageAmount FROM usages WHERE userID = %s AND meterID = %s AND deviceID = %s ORDER BY date"
        data = self.db_helper.fetch_all(query, (self.userID, selected_meter_id, selected_device_id))

        dates = [row[0] for row in data]
        usage_amounts = [row[1] for row in data]

        GraphHelper(self.ui.graphicsDeviceConsumptionAnalysis).draw_graph(dates, usage_amounts, 'Line Graph', 'deviceConsumptionAnalysis')
    
    def load_consumption_analytics(self):
        # Populate the Graph Type combo boxes
        graph_types = ['Bar Graph', 'Pie Chart']
        UIHelper.update_combo_box(self.ui.comboDailyDeviceUsage_GraphType, graph_types)
        UIHelper.update_combo_box(self.ui.comboHistoricalDeviceUsage_GraphType, graph_types)

        # Update the Date combo box for the selected Meter ID
        self.update_daily_device_usage_date()

    def update_daily_device_usage_date(self):
        selected_meter_id = self.ui.comboDailyDeviceUsage_Meter.currentText()
        query = """
            SELECT DISTINCT date 
            FROM usages 
            WHERE userID = %s AND meterID = %s
            ORDER BY date
        """
        dates = [str(item[0]) for item in self.db_helper.fetch_all(query, (self.userID, selected_meter_id))]
        UIHelper.update_combo_box(self.ui.comboDailyDeviceUsage_Date, dates)

    def draw_daily_device_usage(self):
        selected_meter_id = self.ui.comboDailyDeviceUsage_Meter.currentText()
        selected_date = self.ui.comboDailyDeviceUsage_Date.currentText()
        graph_type = self.ui.comboDailyDeviceUsage_GraphType.currentText()

        # Check if a valid date is selected
        if selected_date:
            query = """
                SELECT devicedetails.DeviceName, SUM(usages.usageAmount) 
                FROM usages 
                JOIN devicedetails ON usages.deviceID = devicedetails.DeviceID
                WHERE usages.userID = %s AND usages.meterID = %s AND usages.date = %s
                GROUP BY usages.deviceID
            """
            data = self.db_helper.fetch_all(query, (self.userID, selected_meter_id, selected_date))
            device_names = [item[0] for item in data]
            usage_amounts = [item[1] for item in data]

            graph_helper = GraphHelper(self.ui.graphicsDailyDeviceUsage)
            graph_helper.draw_graph(device_names, usage_amounts, graph_type, 'dailyDeviceUsage')

    def draw_historical_device_usage(self):
        selected_meter_id = self.ui.comboHistoricalDeviceUsage_Meter.currentText()
        graph_type = self.ui.comboHistoricalDeviceUsage_GraphType.currentText()
        query = """
            SELECT devicedetails.DeviceName, SUM(usages.usageAmount) 
            FROM usages 
            JOIN devicedetails ON usages.deviceID = devicedetails.DeviceID
            WHERE usages.userID = %s AND usages.meterID = %s
            GROUP BY usages.deviceID
        """
        data = self.db_helper.fetch_all(query, (self.userID, selected_meter_id))
        device_names = [item[0] for item in data]
        usage_amounts = [item[1] for item in data]

        graph_helper = GraphHelper(self.ui.graphicsHistoricalDeviceUsage)
        graph_helper.draw_graph(device_names, usage_amounts, graph_type, 'historicalDeviceUsage')
    
    def load_energy_insights(self):
        self.draw_daily_energy_overview()
        self.draw_monthly_energy_overview()
        
    def draw_daily_energy_overview(self):
        selected_meter_id = self.ui.comboDailyEnergyOverview_Meter.currentText()
        graph_type = self.ui.comboDailyEnergyOverview_GraphType.currentText()

        query = """
            SELECT DATE(usages.date), SUM(usages.usageAmount * devicedetails.`PowerConsumption (per Hour)`) 
            FROM usages 
            JOIN devicedetails ON usages.deviceID = devicedetails.DeviceID
            WHERE usages.userID = %s AND usages.meterID = %s
            GROUP BY DATE(usages.date)
            ORDER BY DATE(usages.date)
        """
        data = self.db_helper.fetch_all(query, (self.userID, selected_meter_id))
        dates = [item[0] for item in data]
        usage_amounts = [item[1] for item in data]
        GraphHelper(self.ui.graphicsDailyEnergyOverview).draw_graph(dates, usage_amounts, graph_type, 'dailyEnergyOverview')

        prediction, error_message = predict_next_day_usage(self.userID, selected_meter_id)    
        if prediction is None:
            self.ui.labelDailyEnergyOverviewPrediction.setText(error_message or "No usage data available for prediction.")
        else:
            self.ui.labelDailyEnergyOverviewPrediction.setText(f"Next Day Prediction: {prediction:.2f} kWh")
            # # Calculate the next day prediction
        # query = """
        #     SELECT AVG(usageAmount)
        #     FROM (
        #         SELECT SUM(usages.usageAmount * devicedetails.`PowerConsumption (per Hour)`) as usageAmount
        #         FROM usages 
        #         JOIN devicedetails ON usages.deviceID = devicedetails.DeviceID
        #         WHERE usages.userID = %s AND usages.meterID = %s AND DAYOFWEEK(usages.date) = DAYOFWEEK(CURDATE())
        #         GROUP BY DATE(usages.date)
        #     ) as subquery
        # """
        # prediction = self.db_helper.fetch_one(query, (self.userID, selected_meter_id))[0]
        # # Check if the prediction is None
        # if prediction is None:
        #     self.ui.labelDailyEnergyOverviewPrediction.setText("No usage data available for prediction.")
        # else:
        #     self.ui.labelDailyEnergyOverviewPrediction.setText(f"Next Day Prediction: {prediction:.2f}")
    
    def draw_monthly_energy_overview(self):
        selected_meter_id = self.ui.comboMonthlyEnergyOverview_Meter.currentText()
        graph_type = self.ui.comboMonthlyEnergyOverview_GraphType.currentText()

        query = """
            SELECT DATE_FORMAT(usages.date, '%Y-%m'), SUM(usages.usageAmount * devicedetails.`PowerConsumption (per Hour)`) 
            FROM usages 
            JOIN devicedetails ON usages.deviceID = devicedetails.DeviceID
            WHERE usages.userID = %s AND usages.meterID = %s
            GROUP BY DATE_FORMAT(usages.date, '%Y-%m')
            ORDER BY DATE_FORMAT(usages.date, '%Y-%m')
        """
        data = self.db_helper.fetch_all(query, (self.userID, selected_meter_id))
        months = [item[0] for item in data]
        usage_amounts = [item[1] for item in data]
        GraphHelper(self.ui.graphicsMonthlyEnergyOverview).draw_graph(months, usage_amounts, graph_type, 'monthlyEnergyOverview')
    
    def load_billing_details(self):
        self.draw_daily_bill_summary()
        self.draw_monthly_bill_summary()
        
    def draw_daily_bill_summary(self):
        selected_meter_id = self.ui.comboDailyBillSummary_Meter.currentText()
        graph_type = self.ui.comboDailyBillSummary_GraphType.currentText()

        # Get the meter type
        query = """
            SELECT type 
            FROM meter 
            WHERE meterID = %s
        """
        result = self.db_helper.fetch_one(query, (selected_meter_id,))
        if result is None:
            return
        meter_type = result[0]

        # Set the tariff based on the meter type
        tariff = 0.0059 if meter_type == 'Home' else 8

        # Get the daily usage amounts and calculate the cost
        query = """
            SELECT DATE(usages.date), SUM(usages.usageAmount * devicedetails.`PowerConsumption (per Hour)` * %s) 
            FROM usages 
            JOIN devicedetails ON usages.deviceID = devicedetails.DeviceID
            WHERE usages.userID = %s AND usages.meterID = %s
            GROUP BY DATE(usages.date)
            ORDER BY DATE(usages.date)
        """
        data = self.db_helper.fetch_all(query, (tariff, self.userID, selected_meter_id))
        dates = [item[0] for item in data]
        costs = [item[1] for item in data]

        # Draw the graph
        graph_helper = GraphHelper(self.ui.graphicsDailyBillSummary)
        graph_helper.draw_graph(dates, costs, graph_type)

    def draw_monthly_bill_summary(self):
        selected_meter_id = self.ui.comboMonthlyBillSummary_Meter.currentText()
        graph_type = self.ui.comboMonthlyBillSummary_GraphType.currentText()

        # Get the meter type
        query = """
            SELECT type 
            FROM meter 
            WHERE meterID = %s
        """
        result = self.db_helper.fetch_one(query, (selected_meter_id,))
        if result is None:
            return
        meter_type = result[0]

        # Set the tariff based on the meter type
        tariff = 0.0059 if meter_type == 'Home' else 0.008
        # Define a fixed base amount to add to each month's cost
        base_amount = 450  # Example base amount to be added to every month

        # Get the monthly usage amounts and calculate the cost
        query = """
            SELECT DATE_FORMAT(usages.date, '%Y-%m'), SUM(usages.usageAmount * devicedetails.`PowerConsumption (per Hour)` * %s) 
            FROM usages 
            JOIN devicedetails ON usages.deviceID = devicedetails.DeviceID
            WHERE usages.userID = %s AND usages.meterID = %s
            GROUP BY DATE_FORMAT(usages.date, '%Y-%m')
            ORDER BY DATE_FORMAT(usages.date, '%Y-%m')
        """
        data = self.db_helper.fetch_all(query, (tariff, self.userID, selected_meter_id))
        months = [item[0] for item in data]
        costs = [item[1] + base_amount for item in data]  # Add the base amount to each cost

        # Draw the graph
        graph_helper = GraphHelper(self.ui.graphicsMonthlyBillSummary)
        graph_helper.draw_graph(months, costs, graph_type)
        
class AdminPanel(QtWidgets.QMainWindow):
    def __init__(self, admin_username, db):
        super(AdminPanel, self).__init__()
        self.ui = Ui_AdminPanel()
        self.ui.setupUi(self)
        self.db = db
        self.db_helper = DatabaseHelper(db)
        self.admin_username = admin_username
        self.load_admin_info()
        self.load_user_list()
        
        # Connect signals
        self.ui.btnUserList_OpenClient.clicked.connect(self.open_client)
        self.ui.btnUserList_MakeAdmin.clicked.connect(self.make_admin)
        self.ui.btnUserList_DeleteUser.clicked.connect(self.delete_user)
        self.ui.btnUserLIst_ChangePassword.clicked.connect(self.change_password)
        self.ui.btnUserList_ChangeUsername.clicked.connect(self.change_username)
        
        # Filter user list when the input changes
        self.ui.inputUserList_Username.textChanged.connect(self.filter_user_list)

        self.populate_meter_type_combo_boxes()
        self.populate_month_combo_boxes()

        self.ui.comboMonthlyEnergyConsumptionStatistics_MeterType.currentIndexChanged.connect(self.draw_monthly_energy_consumption_statistics)
        self.ui.comboMonthlyEnergyConsumptionStatistics_Month.currentIndexChanged.connect(self.draw_monthly_energy_consumption_statistics)
        self.ui.comboMonthlyEnergyConsumptionStatistics_GraphType.currentIndexChanged.connect(self.draw_monthly_energy_consumption_statistics)
        self.ui.comboTotalEnergyConsumptionStatistics_MeterType.currentIndexChanged.connect(self.draw_total_energy_consumption_statistics)
        self.ui.comboTotalEnergyConsumptionStatistics_GraphType.currentIndexChanged.connect(self.draw_total_energy_consumption_statistics)
        self.ui.tabWidget.currentChanged.connect(self.tab_changed)

        self.draw_monthly_energy_consumption_statistics()
        self.draw_total_energy_consumption_statistics()

        self.resize_timer = QTimer()
        self.resize_timer.setSingleShot(True)
        self.resize_timer.timeout.connect(self.redraw_graphs)

        # Set font bold labelMonthlyEnergyConsumptionStatistics and labelTotalEnergyConsumptionStatistics
        font = QtGui.QFont()
        font.setBold(True)
        self.ui.labelMonthlyEnergyConsumptionStatistics.setFont(font)
        self.ui.labelTotalEnergyConsumptionStatistics.setFont(font)

    def resizeEvent(self, event):
        # Start or restart the timer whenever the window is resized
        self.resize_timer.start(100)  # 500 ms delay

    def redraw_graphs(self):
        # Redraw the graphs
        self.draw_monthly_energy_consumption_statistics()
        self.draw_total_energy_consumption_statistics()
        
    def tab_changed(self, index):
        # Check if the tabConsumptionAnalytics tab is selected
        if self.ui.tabWidget.widget(index) is self.ui.tabStatistics:
            # Redraw the graph
            self.draw_monthly_energy_consumption_statistics()
            self.draw_total_energy_consumption_statistics()
    
    def load_admin_info(self):
        result = self.db_helper.fetch_one("SELECT Fname, Lname FROM users WHERE UserName = %s", (self.admin_username,))
        if result:
            self.ui.labelHeader_FNameandLnameDynamic.setText(f"{result[0]} {result[1]}")
            
    def filter_user_list(self):
        filter_text = self.ui.inputUserList_Username.text()
        for i in range(self.ui.tableUserList.rowCount()):
            item = self.ui.tableUserList.item(i, 1)  # Assuming the username is in the second column
            self.ui.tableUserList.setRowHidden(i, filter_text not in item.text())

    def load_user_list(self):
        results = self.db_helper.fetch_all("SELECT ID, UserName, Fname, Lname, UserType FROM users")
        results = [(str(item[0]), item[1], item[2], item[3], 'Admin' if item[4] == 1 else 'User') for item in results]
        UIHelper.update_table(self.ui.tableUserList, results)
        
    def get_selected_username(self):
        selected_row = self.ui.tableUserList.currentRow()
        if selected_row == -1:
            return ""
        return self.ui.tableUserList.item(selected_row, 1).text()

    def open_client(self):
        username = self.get_selected_username()
        if username == "":
            UIHelper.show_message(self, 'warning', 'Open Client', 'Please select a user.')
            return
        self.main = Main(username, self.db)
        self.main.show()
    
    def make_admin(self):
        username = self.get_selected_username()
        if username == "":
            UIHelper.show_message(self, 'warning', 'Make Admin', 'Please select a user.')
            return
        if username == self.admin_username:
            UIHelper.show_message(self, 'warning', 'Make Admin', 'You cannot change your own admin status.')
            return
        result = self.db_helper.fetch_one("SELECT UserType FROM users WHERE UserName = %s", (username,))
        if result is None:
            UIHelper.show_message(self, 'warning', 'Make Admin', 'User not found.')
            return
        user_type = result[0]
        if user_type == 1:
            reply = UIHelper.show_message(self, 'question', 'Make Admin', 'User is already an admin. Are you sure you want to revoke admin privileges?')
            if reply == QMessageBox.StandardButton.Yes:
                self.db_helper.update("UPDATE users SET UserType = 0 WHERE UserName = %s", (username,))
        elif user_type == 0:
            self.db_helper.update("UPDATE users SET UserType = 1 WHERE UserName = %s", (username,))
        else:
            UIHelper.show_message(self, 'warning', 'Make Admin', 'Invalid user type.')
            return
        self.load_user_list()
        
    def change_password(self):
        username = self.get_selected_username()
        new_password, ok = QInputDialog.getText(self, 'Change Password', 'Enter new password:')
        if ok:
            if new_password.strip() == "":
                UIHelper.show_message(self, 'warning', 'Change Password', 'Password cannot be blank.')
                return
            self.db_helper.update("UPDATE users SET Password = %s WHERE UserName = %s", (new_password, username))
    
    def change_username(self):
        username = self.get_selected_username()
        new_username, ok = QInputDialog.getText(self, 'Change Username', 'Enter new username:')
        if ok:
            if new_username.strip() == "":
                UIHelper.show_message(self, 'warning', 'Change Username', 'Username cannot be blank.')
                return
            if self.db_helper.fetch_one("SELECT UserName FROM users WHERE UserName = %s", (new_username,)) is not None:
                UIHelper.show_message(self, 'warning', 'Change Username', 'Username already exists.')
                return
            self.db_helper.update("UPDATE users SET UserName = %s WHERE UserName = %s", (new_username, username,))
            self.load_user_list()

    def delete_user(self):
        username = self.get_selected_username()
        result = self.db_helper.fetch_one("SELECT ID FROM users WHERE UserName = %s", (username,))
        if result is None:
            UIHelper.show_message(self, 'warning', 'Delete User', 'User not found.')
            return
        user_id = result[0]
        reply = UIHelper.show_message(self, 'question', 'Delete User', 'Are you sure you want to delete this user?')
        if reply == QMessageBox.StandardButton.No:
            return
        self.db_helper.delete("DELETE FROM usersmeters WHERE UserID = %s", (user_id,))
        self.db_helper.delete("DELETE FROM usages WHERE UserID = %s", (user_id,))
        self.db_helper.delete("DELETE FROM usersdevices WHERE UserID = %s", (user_id,))
        self.db_helper.delete("DELETE FROM users WHERE UserName = %s", (username,))
        self.load_user_list()

    def populate_month_combo_boxes(self):
        query = """
            SELECT DISTINCT DATE_FORMAT(date, '%Y-%m') as month
            FROM usages
            ORDER BY month
        """
        data = self.db_helper.fetch_all(query)
        months = [item[0] for item in data]
        UIHelper.update_combo_box(self.ui.comboMonthlyEnergyConsumptionStatistics_Month, months)

    def populate_meter_type_combo_boxes(self):
        query = """
            SELECT DISTINCT type
            FROM meter
        """
        data = self.db_helper.fetch_all(query)
        meter_types = [item[0] for item in data]
        meter_types.insert(0, "All")
        UIHelper.update_combo_box(self.ui.comboMonthlyEnergyConsumptionStatistics_MeterType, meter_types)
        UIHelper.update_combo_box(self.ui.comboTotalEnergyConsumptionStatistics_MeterType, meter_types)

    def draw_monthly_energy_consumption_statistics(self):
        selected_meter_type = self.ui.comboMonthlyEnergyConsumptionStatistics_MeterType.currentText()
        selected_month = self.ui.comboMonthlyEnergyConsumptionStatistics_Month.currentText()
        graph_type = self.ui.comboMonthlyEnergyConsumptionStatistics_GraphType.currentText()
    
        year, month = map(int, selected_month.split('-'))
    
        if selected_meter_type == "All":
            query = """
                SELECT meter.location, SUM(usages.usageAmount * devicedetails.`PowerConsumption (per Hour)`)
                FROM usages
                JOIN devicedetails ON usages.deviceID = devicedetails.DeviceID
                JOIN meter ON usages.meterID = meter.meterID
                WHERE YEAR(usages.date) = %s AND MONTH(usages.date) = %s
                GROUP BY meter.location
            """
            data = self.db_helper.fetch_all(query, (year, month))
        else:
            query = """
                SELECT meter.location, SUM(usages.usageAmount * devicedetails.`PowerConsumption (per Hour)`)
                FROM usages
                JOIN devicedetails ON usages.deviceID = devicedetails.DeviceID
                JOIN meter ON usages.meterID = meter.meterID
                WHERE meter.type = %s AND YEAR(usages.date) = %s AND MONTH(usages.date) = %s
                GROUP BY meter.location
            """
            data = self.db_helper.fetch_all(query, (selected_meter_type, year, month))
    
        locations = [item[0] for item in data]
        usage_amounts = [item[1] for item in data]
        GraphHelper(self.ui.graphicsMonthlyEnergyConsumptionStatistics).draw_graph(locations, usage_amounts, graph_type, 'monthlyEnergyConsumptionStatistics')
    
    def draw_total_energy_consumption_statistics(self):
        selected_meter_type = self.ui.comboTotalEnergyConsumptionStatistics_MeterType.currentText()
        graph_type = self.ui.comboTotalEnergyConsumptionStatistics_GraphType.currentText()
    
        if selected_meter_type == "All":
            query = """
                SELECT meter.location, SUM(usages.usageAmount * devicedetails.`PowerConsumption (per Hour)`)
                FROM usages
                JOIN devicedetails ON usages.deviceID = devicedetails.DeviceID
                JOIN meter ON usages.meterID = meter.meterID
                GROUP BY meter.location
            """
            data = self.db_helper.fetch_all(query)
        else:
            query = """
                SELECT meter.location, SUM(usages.usageAmount * devicedetails.`PowerConsumption (per Hour)`)
                FROM usages
                JOIN devicedetails ON usages.deviceID = devicedetails.DeviceID
                JOIN meter ON usages.meterID = meter.meterID
                WHERE meter.type = %s
                GROUP BY meter.location
            """
            data = self.db_helper.fetch_all(query, (selected_meter_type,))
    
        locations = [item[0] for item in data]
        usage_amounts = [item[1] for item in data]
        GraphHelper(self.ui.graphicsTotalEnergyConsumptionStatistics).draw_graph(locations, usage_amounts, graph_type, 'totalEnergyConsumptionStatistics')

if __name__ == "__main__":
    import sys
    print("[DEBUG] Starting application...")
    app = QtWidgets.QApplication(sys.argv)
    print("[DEBUG] QApplication created successfully")
    
    print("[DEBUG] Attempting to create database connection...")
    if not create_connection():
        print("[ERROR] Database connection failed, exiting...")
        sys.exit(-1)
    print("[DEBUG] Database connection successful")
    
    print("[DEBUG] Creating Login window...")
    login = Login()
    print("[DEBUG] Login window created")
    
    print("[DEBUG] Showing Login window...")
    login.show()
    print("[DEBUG] Login window shown, starting event loop...")
    
    sys.exit(app.exec())