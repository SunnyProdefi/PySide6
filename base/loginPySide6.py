from PySide6.QtWidgets import QApplication, QDialog
from loginBox import Ui_dialog

class MyMainWindow(QDialog, Ui_dialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.pushButton.clicked.connect(self.login)

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        print(f"Username: {username}")
        print(f"Password: {password}")

        if username == "admin" and password == "admin":
            print("Login successful!")
        else:
            print("Login failed!")

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec()