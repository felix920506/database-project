from PyQt6.QtWidgets import QLineEdit, QPushButton, QLabel, QWidget, QFormLayout, QDialog, QStackedLayout
import database

# class loginDialog(QDialog):
#     def __init__(self, parent = None):
#         super(QWidget, self).__init__(parent=parent)
#         layout = QStackedLayout()
#         layout.addWidget(loginFormWidget())
#         self.setLayout(layout)

class loginDialog(QDialog):
    def __init__(self, parent = None):
        super(QWidget, self).__init__(parent=parent)
        layout = QFormLayout(self)

        serverAccountLabel = QLabel(self)
        serverAccountLabel.setText('Database Account')
        self.serverAccountInput = QLineEdit(self)
        layout.addRow(serverAccountLabel, self.serverAccountInput)

        serverPasswordLabel = QLabel(self)
        serverPasswordLabel.setText('Database Password')
        self.serverPasswordInput = QLineEdit(self)
        self.serverPasswordInput.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addRow(serverPasswordLabel, self.serverPasswordInput)

        userIdLabel = QLabel(self)
        userIdLabel.setText('User ID')
        self.userIdInput = QLineEdit(self)
        layout.addRow(userIdLabel, self.userIdInput)

        self.loginUserButton = QPushButton(self)
        self.loginUserButton.setText('Login As User')
        self.loginUserButton.clicked.connect(self.login_as_client)

        self.loginAdminButton = QPushButton(self)
        self.loginAdminButton.setText('Login As Admin')
        self.loginAdminButton.clicked.connect(self.login_as_admin)
        layout.addRow(self.loginUserButton, self.loginAdminButton)

        self.setLayout(layout)
    
    def login_as_admin(self):
        self.connect_to_database()

    def login_as_client(self):
        self.connect_to_database()
        database.setUserId(int(self.userIdInput.text()))

    def connect_to_database(self):

        account = self.serverAccountInput.text()
        password = self.serverPasswordInput.text()

        database.connect(account, password)

        self.close()