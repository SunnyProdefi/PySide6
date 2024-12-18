from PySide6.QtWidgets import QApplication, QWidget, QCheckBox

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ComboBox")
        self.setGeometry(100, 100, 300, 100)
        self.cheakBox = QCheckBox("Python", self)
        self.cheakBox.move(50, 30)
        self.cheakBox.stateChanged.connect(self.selectionChanged)

    def selectionChanged(self,state): 
        if state == 2:
            print(f"Selected: {self.cheakBox.text()}")
        else:
            print(f"Unselected: {self.cheakBox.text()}")

if __name__ == "__main__":
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec()