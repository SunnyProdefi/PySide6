from PySide6.QtWidgets import QApplication, QWidget, QComboBox

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ComboBox")
        self.setGeometry(100, 100, 300, 100)
        self.combo = QComboBox(self)
        self.combo.addItem("Python")
        self.combo.addItem("Java")
        self.combo.addItem("C++")
        self.combo.addItem("C#")
        self.combo.move(50, 30)
        self.combo.currentIndexChanged.connect(self.selectionChanged)

    def selectionChanged(self):
        print(f"Selected: {self.combo.currentText()}")

if __name__ == "__main__":
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec()