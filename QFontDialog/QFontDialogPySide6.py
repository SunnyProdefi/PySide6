import sys
from PySide6.QtWidgets import QApplication, QWidget, QFontDialog
from PySide6.QtGui import QFont

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("字体选择示例")
        self.show()

        # 调用静态方法弹出字体选择框
        ok, font = QFontDialog.getFont()
        if ok:
            print("用户选择的字体：", font.family(), "字号：", font.pointSize())
        else:
            print("用户取消了选择")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())