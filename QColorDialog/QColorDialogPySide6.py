import sys
from PySide6.QtWidgets import QApplication, QWidget, QColorDialog
from PySide6.QtGui import QColor

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("颜色选择示例")
        self.show()

        # 使用静态方法弹出颜色选择框
        color = QColorDialog.getColor(QColor("#00ff00"), self, "请选择颜色")
        if color.isValid():
            print("用户选择的颜色是：", color.name())
        else:
            print("用户未选择有效颜色。")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())
