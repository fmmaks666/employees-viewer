import sqlite3 as sql
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QDialog
from PySide6.QtGui import QPixmap
from uiE import Ui_window
from uiConf import Ui_Configuration

db = sql.connect("employees.db")
c = sql.Cursor(db)
# c.execute("""CREATE TABLE IF NOT EXISTS criminals(id INTEGER PRIMARY KEY, name TEXT, email TEXT, reason TEXT)""")
c.execute("""SELECT * FROM employees""")
# db.commit()

class Configuration(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.dbIP = ""
        self.dbPort = ""
        self.ui = Ui_Configuration()
        self.ui.setupUi(self)
        self.apply = self.ui.apply
        self.ip = self.ui.ipaddr
        self.port = self.ui.dbport
        self.ip.textChanged.connect(self.allowApply)
        self.port.textChanged.connect(self.allowApply)
        self.apply.clicked.connect(self.finish)
    def clear(self):
        self.ip.setText("")
        self.port.setText("")
        self.apply.setEnabled(False)
    def finish(self):
        self.dbIP = self.ip.text()
        self.dbPort = self.port.text()
        self.close()
    def allowApply(self):
        self.apply.setEnabled(bool(self.ip.text().strip() and self.port.text().strip()))
class employeesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        c.execute("""SELECT * FROM employees""")
        self.data = c.fetchall()
        self.id = 0
        # print(f"{self.id=}, {self.data=}, {self.data[self.id][0]=}")
        # initializing compiled UI's object
        self.ui = Ui_window()
        # running setupUi from UI's object
        self.ui.setupUi(self)
        self.conf = Configuration()
        self.name = self.ui.name
        self.age = self.ui.age
        self.schedule = self.ui.schedule
        self.phone = self.ui.phone
        self.email = self.ui.email
        self.photo = self.ui.photo
        self.save = self.ui.save
        self.remove = self.ui.remove
        self.settings = self.ui.settings
        self.connected = self.ui.conn
        self.connected.setText("Not connected")
        self.name.setText("Name: " + self.data[self.id][1])
        self.age.setText("Age: " + str(self.data[self.id][2]))
        self.schedule.setText("Schedule: " + self.data[self.id][3])
        self.phone.setText("Phone: " + self.data[self.id][4])
        self.email.setText("Email: " + self.data[self.id][5])
        self.photo.setPixmap(QPixmap(u"Photos/{}".format(self.data[self.id][6])))
        self.error = self.ui.error
        self.error.hide()
        self.buttonPrev = self.ui.prev
        self.buttonNext = self.ui.next
        if self.id == 0:
            self.buttonPrev.setEnabled(False)
        self.buttonNext.clicked.connect(self.chooseRight)
        self.buttonPrev.clicked.connect(self.chooseLeft)
        self.save.clicked.connect(self.handleSave)
        self.remove.clicked.connect(self.deleteEntry)
        self.settings.clicked.connect(self.config)
        self.conf.apply.clicked.connect(self.updateConnection)
    def handleSave(self):
        db.commit()
        print("[Committed]")
        c.execute("""SELECT * FROM employees""")
        self.data = c.fetchall()
        if self.data == 0:
            self.showError("No entries found in database", True)

    def showError(self, text="No entries found in database", commited=False):
        self.error.show()
        self.error.setText(text)
        self.photo.hide()
        self.name.hide()
        self.phone.hide()
        self.schedule.hide()
        self.email.hide()
        self.age.hide()
        self.buttonNext.setEnabled(False)
        self.buttonPrev.setEnabled(False)
        self.remove.setEnabled(False)
        if commited:
            self.save.setEnabled(False)
    def config(self):
        self.conf.show()
        self.conf.clear()
        # self.conf.ip.setText("Your IP has been leaked!")
        # print(self.conf.ip.text())
    def updateConnection(self):
        if not (self.conf.dbIP.strip() == ""):
            self.connected.setText(f"Connected to: {self.conf.dbIP.strip()}")
            self.connected.adjustSize()
            self.error.hide()
            self.error.setText("-")
            self.photo.show()
            self.name.show()
            self.phone.show()
            self.schedule.show()
            self.email.show()
            self.age.show()
            self.buttonNext.setEnabled(True)
            self.buttonPrev.setEnabled(True)
            self.remove.setEnabled(True)
            if commited:
                self.save.setEnabled(True)
    def chooseRight(self, reset=False):
        self.idWorks()
        # print(f"Momiji, take this chocolate and {self.data=}")
        # print(f"{len(self.data)=}")
        if len(self.data) == 1: return self.labelUpdader()
        if not self.idWorks(): return
        if not reset:
            self.id += 1
        else:
            self.id = 0
        # print(f"\n{self.id=}, {self.data[self.id][0]=}, {self.data=}")
        self.buttonPrev.setEnabled(True)
        if self.id == len(self.data) - 1:
        #self.data = c.fetchall()
        #c.execute("""SELECT * FROM employees""")
            self.buttonNext.setEnabled(False)
        self.name.setText("Name: " + self.data[self.id][1])
        self.age.setText("Age: " + str(self.data[self.id][2]))
        self.schedule.setText("Schedule: " + self.data[self.id][3])
        self.phone.setText("Phone: " + self.data[self.id][4])
        self.email.setText("Email: " + self.data[self.id][5])
        self.photoPath = self.data[self.id][6]

        self.photo.setPixmap(QPixmap(u"Photos/{}".format(self.data[self.id][6])))
    def chooseLeft(self, reset=False):
        # print(f"Momiji, take this chocolate and {self.data=}")
        self.idWorks()
        if not self.idWorks(): return
        if len(self.data) == 1: return self.labelUpdader()
        if not reset:
            self.id -= 1
        else:
            self.id = 0
        # print(f"\n{self.id=}, {self.data[self.id][0]=}, {self.data=}")
        self.buttonNext.setEnabled(True)
        if self.id == 0:
            self.buttonPrev.setEnabled(False)
        #self.data = c.fetchall()
        #c.execute("""SELECT * FROM employees""")
        self.name.setText("Name: " + self.data[self.id][1])
        self.age.setText("Age: " + str(self.data[self.id][2]))
        self.schedule.setText("Schedule: " + self.data[self.id][3])
        self.phone.setText("Phone: " + self.data[self.id][4])
        self.email.setText("Email: " + self.data[self.id][5])
        self.photo.setPixmap(QPixmap(u"Photos/{}".format(self.data[self.id][6])))
    def idWorks(self):
        if len(self.data) == 1:
            self.buttonNext.setDisabled(True)
            self.buttonPrev.setDisabled(True)
            self.id = 0
            self.labelUpdader()
            return False
        return True

    def labelUpdader(self):
        self.name.setText("Name: " + self.data[self.id][1])
        self.age.setText("Age: " + str(self.data[self.id][2]))
        self.schedule.setText("Schedule: " + self.data[self.id][3])
        self.phone.setText("Phone: " + self.data[self.id][4])
        self.email.setText("Email: " + self.data[self.id][5])
        self.photo.setPixmap(QPixmap(u"Photos/{}".format(self.data[self.id][6])))

    def deleteEntry(self):
        self.idWorks()
        # print(f"${self.id=}, {self.data=} | ", end="")
        # print(f"&{self.data[self.id][0]=}")
        query = """DELETE FROM employees WHERE id = ?"""
        if len(self.data) > 0:
            c.execute(query, str(self.data[self.id][0]))
            del self.data[self.id]
            self.idWorks()
            if len(self.data) == 0:
                # print(f"@{len(self.data)=}, {self.data=}")
                self.showError()
                self.idWorks()
                return
            self.chooseLeft(True)

if __name__ == "__main__":
    print("GreyViewers: EmployeesViewer[Momiji Edition]\nStarting...")
    app = QtWidgets.QApplication([])
    window = employeesWindow()
    window.show()
    # window.raise_() to raise window on front of others
    app.setStyle("Breeze")
    app.exec()
