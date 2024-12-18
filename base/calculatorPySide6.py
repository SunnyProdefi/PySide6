from PySide6.QtWidgets import QApplication, QWidget
from Ui_calculator import Ui_Form

class MyMainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.bind()

    def bind(self):
        self.pushButton_0.clicked.connect(lambda: self.lineEdit.insert("0"))
        self.pushButton_1.clicked.connect(lambda: self.lineEdit.insert("1"))
        self.pushButton_2.clicked.connect(lambda: self.lineEdit.insert("2"))
        self.pushButton_3.clicked.connect(lambda: self.lineEdit.insert("3"))
        self.pushButton_4.clicked.connect(lambda: self.lineEdit.insert("4"))
        self.pushButton_5.clicked.connect(lambda: self.lineEdit.insert("5"))
        self.pushButton_6.clicked.connect(lambda: self.lineEdit.insert("6"))
        self.pushButton_7.clicked.connect(lambda: self.lineEdit.insert("7"))
        self.pushButton_8.clicked.connect(lambda: self.lineEdit.insert("8"))
        self.pushButton_9.clicked.connect(lambda: self.lineEdit.insert("9"))
        self.pushButton_dot.clicked.connect(lambda: self.lineEdit.insert("."))
        self.pushButton_add.clicked.connect(lambda: self.lineEdit.insert("+"))
        self.pushButton_sub.clicked.connect(lambda: self.lineEdit.insert("-"))
        self.pushButton_mul.clicked.connect(lambda: self.lineEdit.insert("*"))
        self.pushButton_div.clicked.connect(lambda: self.lineEdit.insert("/"))
        self.pushButton_enter.clicked.connect(self.calculate)
        self.pushButton_clear.clicked.connect(lambda: self.lineEdit.clear())
        self.pushButton_back.clicked.connect(lambda: self.lineEdit.backspace())

    def calculate(self):
        try:
            result = eval(self.lineEdit.text())
            self.lineEdit.setText(str(result))
        except Exception as e:
            self.lineEdit.setText(str(e))

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec()

