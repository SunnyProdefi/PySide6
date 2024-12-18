from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PySide6.QtCore import Qt

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton("Click me!", self)
        btn.setGeometry(0, 0, 200, 100)
        btn.setText("点我！")

        label = QLabel("Hello, World!", self)
        label.setGeometry(0, 100, 200, 100)
        label.setText("你好，世界！")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        line = QLineEdit(self)
        line.setGeometry(0, 200, 200, 100)
        line.setPlaceholderText("请输入内容")


if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec()

