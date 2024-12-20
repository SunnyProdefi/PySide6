# import sys
# from PySide6.QtWidgets import QApplication, QMessageBox, QWidget

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle("My Window")
#         self.show()
#         # 显示一个信息提示框
#         QMessageBox.information(self, "提示", "操作已完成！")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     sys.exit(app.exec())

import sys
from PySide6.QtWidgets import QApplication, QMessageBox, QWidget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("示例窗口")
        self.show()

        # 创建一个QMessageBox实例
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("确认操作")
        msg_box.setText("您确定要删除此文件吗？")

        # 设置消息框的图标
        msg_box.setIcon(QMessageBox.Question)

        # 添加标准按钮
        yes_button = msg_box.addButton("是", QMessageBox.YesRole)
        no_button = msg_box.addButton("否", QMessageBox.NoRole)

        # 设置详细信息区域
        msg_box.setDetailedText("该操作将永久删除文件，且无法恢复。")

        # 显示消息框并获取用户点击的按钮
        msg_box.exec()

        if msg_box.clickedButton() == yes_button:
            print("用户选择是，执行删除操作。")
        else:
            print("用户取消操作。")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())
