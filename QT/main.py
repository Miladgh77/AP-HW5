import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication , QMainWindow
import os

connection=sqlite3.connect("C:/Users/Asus/Desktop/QT/Database/locations.db")
login = uic.loadUiType(os.path.join(os.getcwd(), 'login.ui'))[0]
register = uic.loadUiType(os.path.join(os.getcwd(), 'register.ui'))[0]
location = uic.loadUiType(os.path.join(os.getcwd(), 'location.ui'))[0]

connection.execute("CREATE TABLE if not exists users (id integer primary key autoincrement, name text, phone integer, username text, password text)")


class Location(location, QMainWindow):
    def __init__(self):
        location.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)


class Register(register, QMainWindow):
    def __init__(self):
        register.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.make_user)

    def make_user(self):
        stmt = "INSERT INTO users(name, phone, username, password)values(?, ?, ?, ?)"
        args = (self.name.displayText(), self.phone.displayText(), self.username.displayText(), self.password.displayText())
        connection.execute(stmt, args)
        connection.commit()
        self.hide()


class Login(login, QMainWindow):
    def __init__(self, x):
        login.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.pushButton_2.clicked.connect(x.show)
        self.pushButton.clicked.connect(self.check)

    def check(self):
        stmt = "SELECT password FROM users WHERE username = (?)"
        args = (self.username.displayText(), )
        cursor = connection.execute(stmt, args)
        for row in cursor:
             if self.password.displayText() == row[0]:
                 print("true")
             else:
                 print("false")


app = QApplication(sys.argv)
loc = Location()
reg = Register()
log = Login(reg)
log.show()
sys.exit(app.exec_())
