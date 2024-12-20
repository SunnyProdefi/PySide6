import sys
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("示例窗口")
        self.show()

        filename, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "Text Files (*.txt);;All Files (*)")
        if filename:
            print("选择的文件是：", filename)
        else:
            print("用户未选择文件。")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())