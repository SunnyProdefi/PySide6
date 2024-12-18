from PySide6.QtWidgets import QApplication, QWidget
from Ui_baseConverter import Ui_Form

class BaseConverter(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 初始化数据类型下拉框
        self.dataTypeComboBox.addItems(['长度', '重量'])
        
        # 连接信号和槽
        self.oneInputLineEdit.textChanged.connect(self.oneInputChanged)
        self.twoInputLineEdit.textChanged.connect(self.twoInputChanged)
        self.dataTypeComboBox.currentIndexChanged.connect(self.dataTypeChanged)
        self.oneInputComboBox.currentIndexChanged.connect(self.oneInputChanged)
        self.twoInputComboBox.currentIndexChanged.connect(self.twoInputChanged)

        # 初始化时根据当前dataTypeComboBox更新单位
        self.dataTypeChanged(self.dataTypeComboBox.currentIndex())

    def dataTypeChanged(self, index):
        """
        当选择的数据类型变化时，更改单位选项。
        index = 0: 长度
        index = 1: 重量
        """
        self.oneInputComboBox.clear()
        self.twoInputComboBox.clear()

        if index == 0:
            # 长度单位：米(m)、千米(km)、厘米(cm)、毫米(mm)
            units = ["米(m)", "千米(km)", "厘米(cm)", "毫米(mm)"]
        else:
            # 重量单位：千克(kg)、克(g)、磅(lb)、盎司(oz)
            units = ["千克(kg)", "克(g)", "磅(lb)", "盎司(oz)"]

        self.oneInputComboBox.addItems(units)
        self.twoInputComboBox.addItems(units)

        # 当数据类型变化后，重新进行转换计算
        self.oneInputChanged()

    def oneInputChanged(self):
        """
        当oneInputLineEdit或相关单位发生变化时，将oneInput对应的数值转换成twoInput对应的单位并显示在twoInputLineEdit中。
        同时在rawDataLabel显示原始数值与原始单位，在transformDataLabel显示转换后的值与转换后单位。
        """
        input_text = self.oneInputLineEdit.text().strip()
        if not input_text:
            self.twoInputLineEdit.clear()
            self.rawDataLabel.clear()
            self.transformDataLabel.clear()
            return
        try:
            value = float(input_text)
        except ValueError:
            self.twoInputLineEdit.setText("输入错误")
            self.rawDataLabel.setText("输入错误")
            self.transformDataLabel.clear()
            return

        data_type = self.dataTypeComboBox.currentIndex()
        from_unit = self.oneInputComboBox.currentIndex()
        to_unit = self.twoInputComboBox.currentIndex()

        result = self.convert(value, data_type, from_unit, to_unit)

        # 更新twoInputLineEdit
        self.twoInputLineEdit.setText(str(result))
        # 更新rawDataLabel和transformDataLabel
        self.rawDataLabel.setText(f"{value} {self.oneInputComboBox.currentText()}" + " = ")
        self.transformDataLabel.setText(f"{result} {self.twoInputComboBox.currentText()}")

    def twoInputChanged(self):
        """
        当twoInputLineEdit或相关单位发生变化时，将twoInput对应的数值转换成oneInput对应的单位并显示在oneInputLineEdit中。
        同时更新rawDataLabel和transformDataLabel。
        """
        input_text = self.twoInputLineEdit.text().strip()
        if not input_text:
            self.oneInputLineEdit.clear()
            self.rawDataLabel.clear()
            self.transformDataLabel.clear()
            return
        try:
            value = float(input_text)
        except ValueError:
            self.oneInputLineEdit.setText("输入错误")
            self.rawDataLabel.setText("输入错误")
            self.transformDataLabel.clear()
            return

        data_type = self.dataTypeComboBox.currentIndex()
        from_unit = self.twoInputComboBox.currentIndex()
        to_unit = self.oneInputComboBox.currentIndex()

        result = self.convert(value, data_type, from_unit, to_unit)

        # 更新oneInputLineEdit
        self.oneInputLineEdit.setText(str(result))
        # 更新rawDataLabel和transformDataLabel
        self.rawDataLabel.setText(f"{value} {self.twoInputComboBox.currentText()}")
        self.transformDataLabel.setText(f"{result} {self.oneInputComboBox.currentText()}")

    def convert(self, value, data_type, from_unit, to_unit):
        """
        将value从from_unit所表示的单位转换为to_unit对应的单位。
        
        data_type: 0表示长度，1表示重量
        from_unit, to_unit: 对应下拉框中的选项序号
        """
        # 根据data_type选择转换基准：长度以米(m)为基准，重量以千克(kg)为基准
        if data_type == 0:  # 长度
            # 对应顺序: 米(m)、千米(km)、厘米(cm)、毫米(mm)
            factors = [1.0, 1000.0, 0.01, 0.001]  
        else:  # 重量
            # 对应顺序：千克(kg)、克(g)、磅(lb)、盎司(oz)
            factors = [1.0, 0.001, 0.45359237, 0.028349523125]

        # 先将待转换值统一转换成基准单位(米或千克)
        base_value = value * factors[from_unit]

        # 再从基准单位转换到目标单位
        result = base_value / factors[to_unit]

        return result

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = BaseConverter()
    window.show()
    sys.exit(app.exec())
