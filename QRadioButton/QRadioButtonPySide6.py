from PySide6.QtWidgets import QApplication, QWidget, QRadioButton, QVBoxLayout, QButtonGroup, QLabel
import sys

def on_button_toggled():
    # 遍历所有选项，找到当前被选中的单选按钮
    for btn in (radio1, radio2, radio3):
        if btn.isChecked():
            label.setText(f"当前选中：{btn.text()}")

app = QApplication(sys.argv)

window = QWidget()
layout = QVBoxLayout(window)

radio1 = QRadioButton("选项 A")
radio2 = QRadioButton("选项 B")
radio3 = QRadioButton("选项 C")

# 创建一个按钮组，并将三个单选按钮加入其中
group = QButtonGroup(window)
group.addButton(radio1)
group.addButton(radio2)
group.addButton(radio3)

radio1.toggled.connect(on_button_toggled)
radio2.toggled.connect(on_button_toggled)
radio3.toggled.connect(on_button_toggled)

# 设置初始状态
radio1.setChecked(True)

label = QLabel("当前选中：选项 A")

layout.addWidget(radio1)
layout.addWidget(radio2)
layout.addWidget(radio3)
layout.addWidget(label)

window.setLayout(layout)
window.show()
sys.exit(app.exec())