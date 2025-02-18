# from PyQt6 import QtCore, QtGui, QtWidgets

# class Ui_RegisterPage(object):
#     def setupUi(self, RegisterPage):
#         RegisterPage.setObjectName("RegisterPage")
#         RegisterPage.resize(1200, 1200)
#         RegisterPage.setWindowTitle("Register - PowerWatch")
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap(":/svg/powerwatch_logo.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
#         RegisterPage.setWindowIcon(icon)
#         RegisterPage.setStyleSheet("* {\n"
# "background-color: #111010;\n"
# "color: white;\n"
# "}")
#         self.centralwidget = QtWidgets.QWidget(parent=RegisterPage)
#         self.centralwidget.setStyleSheet("QPushButton { \n"
# "padding: 3px;\n"
# "border-color: white;\n"
# "border: 1px solid white;\n"
# "color: black;\n"
# "background-color: white;\n"
# "\n"
# "}\n"
# "\n"
# "QPushButton:enabled {\n"
# "  background-color: #facc15; /* Yellow shade */\n"
# "  color: black; /* Text color */\n"
# "border-radius: 3px;\n"
# "}\n"
# "\n"
# "QPushButton:pressed {\n"
# "    background-color: #facc15;\n"
# "        color: #000000;\n"
# "}\n"
# "\n"
# "\n"
# "QPushButton:hover:!pressed {\n"
# "        background-color: #6d28d9;\n"
# "}\n"
# "\n"
# "QPushButton:disabled {\n"
# "        background-color: grey;\n"
# "}")
#         self.centralwidget.setObjectName("centralwidget")
#         self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
#         self.verticalLayout_3.setObjectName("verticalLayout_3")
#         self.frame = QtWidgets.QFrame(parent=self.centralwidget)
#         self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
#         self.frame.setObjectName("frame")
#         self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame)
#         self.verticalLayout_7.setObjectName("verticalLayout_7")
#         self.widgetHeader = QtWidgets.QWidget(parent=self.frame)
#         self.widgetHeader.setMinimumSize(QtCore.QSize(400, 0))
#         self.widgetHeader.setObjectName("widgetHeader")
#         self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widgetHeader)
#         self.horizontalLayout_2.setObjectName("horizontalLayout_2")
#         self.labelLogo = QtWidgets.QLabel(parent=self.widgetHeader)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.labelLogo.sizePolicy().hasHeightForWidth())
#         self.labelLogo.setSizePolicy(sizePolicy)
#         self.labelLogo.setMaximumSize(QtCore.QSize(30, 30))
#         self.labelLogo.setText("")
#         self.labelLogo.setPixmap(QtGui.QPixmap(":/svg/powerwatch_logo.svg"))
#         self.labelLogo.setScaledContents(True)
#         self.labelLogo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
#         self.labelLogo.setObjectName("labelLogo")
#         self.horizontalLayout_2.addWidget(self.labelLogo)
#         self.verticalLayout_7.addWidget(self.widgetHeader, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
#         self.frameMain = QtWidgets.QFrame(parent=self.frame)
#         self.frameMain.setMinimumSize(QtCore.QSize(300, 0))
#         self.frameMain.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
#         self.frameMain.setObjectName("frameMain")
#         self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frameMain)
#         self.verticalLayout_6.setObjectName("verticalLayout_6")
#         self.frameName = QtWidgets.QFrame(parent=self.frameMain)
#         self.frameName.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
#         self.frameName.setObjectName("frameName")
#         self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frameName)
#         self.verticalLayout_5.setSpacing(0) 
#         self.verticalLayout_5.setObjectName("verticalLayout_5")
#         self.labelName = QtWidgets.QLabel(parent=self.frameName)
#         self.labelName.setStyleSheet("")
#         self.labelName.setObjectName("labelName")
#         self.verticalLayout_5.addWidget(self.labelName)
#         self.inputName = QtWidgets.QLineEdit(parent=self.frameName)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.inputName.sizePolicy().hasHeightForWidth())
#         self.inputName.setSizePolicy(sizePolicy)
#         self.inputName.setStyleSheet("padding: 4px;\n"
# "color: black;\n"
# "background-color: white;")
#         self.inputName.setFrame(False)
#         self.inputName.setObjectName("inputName")
#         self.verticalLayout_5.addWidget(self.inputName)
#         self.verticalLayout_6.addWidget(self.frameName)
#         self.frameSurname = QtWidgets.QFrame(parent=self.frameMain)
#         self.frameSurname.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
#         self.frameSurname.setObjectName("frameSurname")
#         self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frameSurname)
#         self.verticalLayout_4.setObjectName("verticalLayout_4")
#         self.labelSurname = QtWidgets.QLabel(parent=self.frameSurname)
#         self.labelSurname.setStyleSheet("")
#         self.labelSurname.setObjectName("labelSurname")
#         self.verticalLayout_4.addWidget(self.labelSurname)
#         self.inputSurname = QtWidgets.QLineEdit(parent=self.frameSurname)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.inputSurname.sizePolicy().hasHeightForWidth())
#         self.inputSurname.setSizePolicy(sizePolicy)
#         self.inputSurname.setStyleSheet("padding: 4px;\n"
# "color: black;\n"
# "background-color: white;")
#         self.inputSurname.setFrame(False)
#         self.inputSurname.setObjectName("inputSurname")
#         self.verticalLayout_4.addWidget(self.inputSurname)
#         self.verticalLayout_6.addWidget(self.frameSurname)
#         self.frameUsername = QtWidgets.QFrame(parent=self.frameMain)
#         self.frameUsername.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
#         self.frameUsername.setObjectName("frameUsername")
#         self.verticalLayout = QtWidgets.QVBoxLayout(self.frameUsername)
#         self.verticalLayout.setObjectName("verticalLayout")
#         self.labelUsername = QtWidgets.QLabel(parent=self.frameUsername)
#         self.labelUsername.setStyleSheet("")
#         self.labelUsername.setObjectName("labelUsername")
#         self.verticalLayout.addWidget(self.labelUsername)
#         self.inputUsername = QtWidgets.QLineEdit(parent=self.frameUsername)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.inputUsername.sizePolicy().hasHeightForWidth())
#         self.inputUsername.setSizePolicy(sizePolicy)
#         self.inputUsername.setStyleSheet("padding: 4px;\n"
# "color: black;\n"
# "background-color: white;")
#         self.inputUsername.setText("")
#         self.inputUsername.setFrame(False)
#         self.inputUsername.setObjectName("inputUsername")
#         self.verticalLayout.addWidget(self.inputUsername)
#         self.verticalLayout_6.addWidget(self.frameUsername)
#         self.framePassword = QtWidgets.QFrame(parent=self.frameMain)
#         self.framePassword.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
#         self.framePassword.setObjectName("framePassword")
#         self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.framePassword)
#         self.verticalLayout_2.setObjectName("verticalLayout_2")
#         self.labelPassword = QtWidgets.QLabel(parent=self.framePassword)
#         self.labelPassword.setStyleSheet("")
#         self.labelPassword.setObjectName("labelPassword")
#         self.verticalLayout_2.addWidget(self.labelPassword)
#         self.inputPassword = QtWidgets.QLineEdit(parent=self.framePassword)
#         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(self.inputPassword.sizePolicy().hasHeightForWidth())
#         self.inputPassword.setSizePolicy(sizePolicy)
#         self.inputPassword.setStyleSheet("padding: 4px;\n"
# "color: black;\n"
# "background-color: white;")
#         self.inputPassword.setFrame(False)
#         self.inputPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
#         self.inputPassword.setObjectName("inputPassword")
#         self.verticalLayout_2.addWidget(self.inputPassword)
#         self.verticalLayout_6.addWidget(self.framePassword)
#         self.frameButtons = QtWidgets.QFrame(parent=self.frameMain)
#         self.frameButtons.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
#         self.frameButtons.setObjectName("frameButtons")
#         self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameButtons)
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.btnRegister = QtWidgets.QPushButton(parent=self.frameButtons)
#         self.btnRegister.setStyleSheet("")
#         self.btnRegister.setObjectName("btnRegister")
#         self.horizontalLayout.addWidget(self.btnRegister)
#         self.verticalLayout_6.addWidget(self.frameButtons)
#         self.verticalLayout_7.addWidget(self.frameMain, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
#         self.verticalLayout_3.addWidget(self.frame)
#         RegisterPage.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(parent=RegisterPage)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 444, 26))
#         self.menubar.setObjectName("menubar")
#         RegisterPage.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(parent=RegisterPage)
#         self.statusbar.setObjectName("statusbar")
#         RegisterPage.setStatusBar(self.statusbar)

#         # Frame for Email
#         self.frameEmail = QtWidgets.QFrame(parent=self.frameMain)
#         self.frameEmail.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
#         self.frameEmail.setObjectName("frameEmail")
#         self.verticalLayoutEmail = QtWidgets.QVBoxLayout(self.frameEmail)
#         self.verticalLayoutEmail.setObjectName("verticalLayoutEmail")
#         self.labelEmail = QtWidgets.QLabel(parent=self.frameEmail)
#         self.labelEmail.setText("Email")  # Label for email field
#         self.labelEmail.setObjectName("labelEmail")
#         self.verticalLayoutEmail.addWidget(self.labelEmail)
#         self.inputEmail = QtWidgets.QLineEdit(parent=self.frameEmail)
#         self.inputEmail.setStyleSheet("padding: 4px;\n"
#                                 "color: black;\n"
#                                 "background-color: white;")
#         self.inputEmail.setFrame(False)
#         self.inputEmail.setObjectName("inputEmail")
#         self.verticalLayoutEmail.addWidget(self.inputEmail)
#         self.verticalLayout_6.addWidget(self.frameEmail)

#         # Frame for Phone Number
#         self.framePhone = QtWidgets.QFrame(parent=self.frameMain)
#         self.framePhone.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
#         self.framePhone.setObjectName("framePhone")
#         self.verticalLayoutPhone = QtWidgets.QVBoxLayout(self.framePhone)
#         self.verticalLayoutPhone.setObjectName("verticalLayoutPhone")
#         self.labelPhone = QtWidgets.QLabel(parent=self.framePhone)
#         self.labelPhone.setText("Phone Number")  # Label for phone field
#         self.labelPhone.setObjectName("labelPhone")
#         self.verticalLayoutPhone.addWidget(self.labelPhone)
#         self.inputPhone = QtWidgets.QLineEdit(parent=self.framePhone)
#         self.inputPhone.setStyleSheet("padding: 4px;\n"
#                                 "color: black;\n"
#                                 "background-color: white;")
#         self.inputPhone.setFrame(False)
#         self.inputPhone.setObjectName("inputPhone")
#         self.verticalLayoutPhone.addWidget(self.inputPhone)
#         self.verticalLayout_6.addWidget(self.framePhone)

#         # Frame for Street Address
#         self.frameStreet = QtWidgets.QFrame(parent=self.frameMain)
#         self.frameStreet.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
#         self.frameStreet.setObjectName("frameStreet")
#         self.verticalLayoutStreet = QtWidgets.QVBoxLayout(self.frameStreet)
#         self.verticalLayoutStreet.setObjectName("verticalLayoutStreet")
#         self.labelStreet = QtWidgets.QLabel(parent=self.frameStreet)
#         self.labelStreet.setText("Street Address")  # Label for street field
#         self.labelStreet.setObjectName("labelStreet")
#         self.verticalLayoutStreet.addWidget(self.labelStreet)
#         self.inputStreet = QtWidgets.QLineEdit(parent=self.frameStreet)
#         self.inputStreet.setStyleSheet("padding: 4px;\n"
#                                 "color: black;\n"
#                                 "background-color: white;")
#         self.inputStreet.setFrame(False)
#         self.inputStreet.setObjectName("inputStreet")
#         self.verticalLayoutStreet.addWidget(self.inputStreet)
#         self.verticalLayout_6.addWidget(self.frameStreet)

#         # Frame for City
#         self.frameCity = QtWidgets.QFrame(parent=self.frameMain)
#         self.frameCity.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
#         self.frameCity.setObjectName("frameCity")
#         self.verticalLayoutCity = QtWidgets.QVBoxLayout(self.frameCity)
#         self.verticalLayoutCity.setObjectName("verticalLayoutCity")
#         self.labelCity = QtWidgets.QLabel(parent=self.frameCity)
#         self.labelCity.setText("City")  # Label for city field
#         self.labelCity.setObjectName("labelCity")
#         self.verticalLayoutCity.addWidget(self.labelCity)
#         self.inputCity = QtWidgets.QLineEdit(parent=self.frameCity)
#         self.inputCity.setStyleSheet("padding: 4px;\n"
#                                 "color: black;\n"
#                                 "background-color: white;")
#         self.inputCity.setFrame(False)
#         self.inputCity.setObjectName("inputCity")
#         self.verticalLayoutCity.addWidget(self.inputCity)
#         self.verticalLayout_6.addWidget(self.frameCity)

#         # Frame for State
#         self.frameState = QtWidgets.QFrame(parent=self.frameMain)
#         self.frameState.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
#         self.frameState.setObjectName("frameState")
#         self.verticalLayoutState = QtWidgets.QVBoxLayout(self.frameState)
#         self.verticalLayoutState.setObjectName("verticalLayoutState")
#         self.labelState = QtWidgets.QLabel(parent=self.frameState)
#         self.labelState.setText("State")  # Label for state field
#         self.labelState.setObjectName("labelState")
#         self.verticalLayoutState.addWidget(self.labelState)
#         self.inputState = QtWidgets.QLineEdit(parent=self.frameState)
#         self.inputState.setStyleSheet("padding: 4px;\n"
#                                 "color: black;\n"
#                                 "background-color: white;")
#         self.inputState.setFrame(False)
#         self.inputState.setObjectName("inputState")
#         self.verticalLayoutState.addWidget(self.inputState)
#         self.verticalLayout_6.addWidget(self.frameState)

#         # Frame for Pincode
#         self.framePincode = QtWidgets.QFrame(parent=self.frameMain)
#         self.framePincode.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
#         self.framePincode.setObjectName("framePincode")
#         self.verticalLayoutPincode = QtWidgets.QVBoxLayout(self.framePincode)
#         self.verticalLayoutPincode.setObjectName("verticalLayoutPincode")
#         self.labelPincode = QtWidgets.QLabel(parent=self.framePincode)
#         self.labelPincode.setText("Pincode")  # Label for pincode field
#         self.labelPincode.setObjectName("labelPincode")
#         self.verticalLayoutPincode.addWidget(self.labelPincode)
#         self.inputPincode = QtWidgets.QLineEdit(parent=self.framePincode)
#         self.inputPincode.setStyleSheet("padding: 4px;\n"
#                                         "color: black;\n"
#                                         "background-color: white;")
#         self.inputPincode.setFrame(False)
#         self.inputPincode.setObjectName("inputPincode")
#         self.verticalLayoutPincode.addWidget(self.inputPincode)
#         self.verticalLayout_6.addWidget(self.framePincode)

#         # After adding these new fields, the "Register" button should appear next
#         self.verticalLayout_6.addWidget(self.frameButtons)


#         self.retranslateUi(RegisterPage)
#         QtCore.QMetaObject.connectSlotsByName(RegisterPage)

#     def retranslateUi(self, RegisterPage):
#         _translate = QtCore.QCoreApplication.translate
#         self.labelName.setText(_translate("RegisterPage", "Name"))
#         self.labelSurname.setText(_translate("RegisterPage", "Surname"))
#         self.labelUsername.setText(_translate("RegisterPage", "Username"))
#         self.labelPassword.setText(_translate("RegisterPage", "Password"))
#         self.btnRegister.setText(_translate("RegisterPage", "Register"))
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_RegisterPage(object):
    def setupUi(self, RegisterPage):
        RegisterPage.setObjectName("RegisterPage")
        RegisterPage.resize(500, 800)  # Adjusted default size
        RegisterPage.setWindowTitle("Register - PowerGauge")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/svg/powerwatch_logo.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        RegisterPage.setWindowIcon(icon)
        RegisterPage.setStyleSheet("* {\n"
"background-color: #111010;\n"
"color: white;\n"
"}")
        
        # Create central widget
        self.centralwidget = QtWidgets.QWidget(parent=RegisterPage)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # Create scroll area
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet("QScrollArea { border: none; }")
        
        # Create scroll content widget
        self.scrollContent = QtWidgets.QWidget()
        self.scrollContent.setObjectName("scrollContent")
        self.verticalLayout_scroll = QtWidgets.QVBoxLayout(self.scrollContent)
        
        # Add the existing frame to the scroll content
        self.frame = QtWidgets.QFrame(parent=self.scrollContent)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame)
        
        # Header widget (logo)
        self.widgetHeader = QtWidgets.QWidget(parent=self.frame)
        self.widgetHeader.setMinimumSize(QtCore.QSize(400, 0))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widgetHeader)  # Fixed: Properly reference the layout
        self.labelLogo = QtWidgets.QLabel(parent=self.widgetHeader)
        self.labelLogo.setMaximumSize(QtCore.QSize(30, 30))
        self.labelLogo.setPixmap(QtGui.QPixmap(":/svg/powerwatch_logo.svg"))
        self.labelLogo.setScaledContents(True)
        self.labelLogo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_2.addWidget(self.labelLogo)  # Fixed: Use self.horizontalLayout_2
        self.verticalLayout_7.addWidget(self.widgetHeader, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)

        # Main content frame
        self.frameMain = QtWidgets.QFrame(parent=self.frame)
        self.frameMain.setMinimumSize(QtCore.QSize(300, 0))
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frameMain)

        # Add all input fields (Name, Surname, Username, etc.)
        self.create_input_field(self.frameMain, "Name", self.verticalLayout_6)
        self.create_input_field(self.frameMain, "Surname", self.verticalLayout_6)
        self.create_input_field(self.frameMain, "Username", self.verticalLayout_6)
        self.create_input_field(self.frameMain, "Password", self.verticalLayout_6, is_password=True)
        self.create_input_field(self.frameMain, "Email", self.verticalLayout_6)
        self.create_input_field(self.frameMain, "Phone", self.verticalLayout_6)
        self.create_input_field(self.frameMain, "Street", self.verticalLayout_6)
        self.create_input_field(self.frameMain, "City", self.verticalLayout_6)
        self.create_input_field(self.frameMain, "State", self.verticalLayout_6)
        self.create_input_field(self.frameMain, "Pincode", self.verticalLayout_6)

        # Register button
        self.frameButtons = QtWidgets.QFrame(parent=self.frameMain)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameButtons)
        self.btnRegister = QtWidgets.QPushButton(parent=self.frameButtons)
        self.btnRegister.setStyleSheet("""
            QPushButton { 
                padding: 3px;
                border-color: white;
                border: 1px solid white;
                color: black;
                background-color: white;
            }
            QPushButton:enabled {
                background-color: #8b5cf6;
                color: black;
                border-radius: 3px;
            }
            QPushButton:pressed {
                background-color: #8b5cf6;
                color: #000000;
            }
            QPushButton:hover:!pressed {
                background-color: #6d28d9;
            }
            QPushButton:disabled {
                background-color: grey;
            }
        """)
        self.btnRegister.setText("Register")
        self.horizontalLayout.addWidget(self.btnRegister)
        self.verticalLayout_6.addWidget(self.frameButtons)

        # Add frameMain to the main layout
        self.verticalLayout_7.addWidget(self.frameMain, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        
        # Set up scroll area
        self.verticalLayout_scroll.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollContent)
        self.verticalLayout_3.addWidget(self.scrollArea)
        
        # Set central widget
        RegisterPage.setCentralWidget(self.centralwidget)
        
        # Menu and status bar
        self.menubar = QtWidgets.QMenuBar(parent=RegisterPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 444, 26))
        RegisterPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=RegisterPage)
        RegisterPage.setStatusBar(self.statusbar)

    def create_input_field(self, parent, label_text, layout, is_password=False):
        frame = QtWidgets.QFrame(parent=parent)
        frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        vertical_layout = QtWidgets.QVBoxLayout(frame)
        
        label = QtWidgets.QLabel(parent=frame)
        label.setText(label_text)
        vertical_layout.addWidget(label)
        
        input_field = QtWidgets.QLineEdit(parent=frame)
        input_field.setStyleSheet("padding: 4px;\ncolor: black;\nbackground-color: white;")
        input_field.setFrame(False)
        if is_password:
            input_field.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        
        vertical_layout.addWidget(input_field)
        layout.addWidget(frame)
        
        # Store the input field as an attribute
        setattr(self, f"input{label_text}", input_field)

def validate_email(self):
    """Validates email format and updates UI feedback."""
    email = self.inputEmail.text()
    is_valid = '@' in email and '.' in email.split('@')[1]
    
    if not email:  # Empty email field
        self.inputEmail.setStyleSheet("padding: 4px;\ncolor: black;\nbackground-color: white;")
        return False
    elif is_valid:
        self.inputEmail.setStyleSheet("padding: 4px;\ncolor: black;\nbackground-color: #90EE90;")  # Light green for valid
        return True
    else:
        self.inputEmail.setStyleSheet("padding: 4px;\ncolor: black;\nbackground-color: #FFB6C1;")  # Light red for invalid
        return False
# def validate_email(self):
#     """Validates email format and checks for existing email in database."""
#     email = self.inputEmail.text()
    
#     # Check empty email
#     if not email:  # Empty email field
#         self.inputEmail.setStyleSheet("padding: 4px;\ncolor: black;\nbackground-color: white;")
#         return False
        
#     # Check email format
#     is_valid_format = '@' in email and '.' in email.split('@')[1]
#     if not is_valid_format:
#         self.inputEmail.setStyleSheet("padding: 4px;\ncolor: black;\nbackground-color: #FFB6C1;")  # Light red for invalid
#         return False
        
#     # Check if email exists in database
#     try:
#         query = "SELECT COUNT(*) FROM users WHERE email = %s"
#         count = self.db_helper.fetch_one(query, (email))[0]
#         print(count)
        
#         if count > 0:
#             self.inputEmail.setStyleSheet("padding: 4px;\ncolor: black;\nbackground-color: #FFB6C1;")  # Light red for duplicate
#             # Show message for duplicate email
#             msg = QtWidgets.QMessageBox()
#             msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
#             msg.setWindowTitle("Email Already Registered")
#             msg.setText("This email is already registered.")
#             msg.setInformativeText("Please use a different email address or login with your existing account.")
#             msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
#             msg.exec()
#             return False
            
#     except Exception as e:
#         print(f"Database error: {e}")
#         return False
    
#     # Email is valid and not registered
#     self.inputEmail.setStyleSheet("padding: 4px;\ncolor: black;\nbackground-color: #90EE90;")  # Light green for valid
#     return True
    
def validate_phone(self):
    """Validates phone number format and updates UI feedback."""
    phone = self.inputPhone.text()
    is_valid = phone.isdigit() and len(phone) == 10
    
    if not phone:  # Empty phone field
        self.inputPhone.setStyleSheet("padding: 4px;\ncolor: black;\nbackground-color: white;")
        return False
    elif is_valid:
        self.inputPhone.setStyleSheet("padding: 4px;\ncolor: black;\nbackground-color: #90EE90;")  # Light green for valid
        return True
    else:
        self.inputPhone.setStyleSheet("padding: 4px;\ncolor: black;\nbackground-color: #FFB6C1;")  # Light red for invalid
        return False


