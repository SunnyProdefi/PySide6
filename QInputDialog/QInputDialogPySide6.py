import sys
from PySide6.QtWidgets import QApplication, QInputDialog, QLineEdit, QWidget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("示例窗口")
        self.show()

        dialog = QInputDialog(self)
        dialog.setWindowTitle("自定义输入对话框")
        dialog.setLabelText("请输入您的姓名：")
        dialog.setTextValue("默认名")

        dialog.setTextEchoMode(QLineEdit.Normal)

        if dialog.exec() == QInputDialog.Accepted:
            text = dialog.textValue()
            print("您输入的姓名是：", text)
        else:
            print("用户取消或未输入。")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())
