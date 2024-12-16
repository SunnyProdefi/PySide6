from PySide6.QtWidgets import QApplication, QDialog
from Ui_calculator import Ui_Form

class MyMainWindow(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec()