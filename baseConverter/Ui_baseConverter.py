# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'baseConverter.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(303, 194)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 20, 231, 144))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.rawDataLabel = QLabel(self.widget)
        self.rawDataLabel.setObjectName(u"rawDataLabel")
        font = QFont()
        font.setPointSize(12)
        self.rawDataLabel.setFont(font)

        self.verticalLayout.addWidget(self.rawDataLabel)

        self.transformDataLabel = QLabel(self.widget)
        self.transformDataLabel.setObjectName(u"transformDataLabel")
        self.transformDataLabel.setFont(font)

        self.verticalLayout.addWidget(self.transformDataLabel)

        self.dataTypeComboBox = QComboBox(self.widget)
        self.dataTypeComboBox.setObjectName(u"dataTypeComboBox")

        self.verticalLayout.addWidget(self.dataTypeComboBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.oneInputLineEdit = QLineEdit(self.widget)
        self.oneInputLineEdit.setObjectName(u"oneInputLineEdit")

        self.horizontalLayout.addWidget(self.oneInputLineEdit)

        self.oneInputComboBox = QComboBox(self.widget)
        self.oneInputComboBox.setObjectName(u"oneInputComboBox")

        self.horizontalLayout.addWidget(self.oneInputComboBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.twoInputLineEdit = QLineEdit(self.widget)
        self.twoInputLineEdit.setObjectName(u"twoInputLineEdit")

        self.horizontalLayout_2.addWidget(self.twoInputLineEdit)

        self.twoInputComboBox = QComboBox(self.widget)
        self.twoInputComboBox.setObjectName(u"twoInputComboBox")

        self.horizontalLayout_2.addWidget(self.twoInputComboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"baseConverter", None))
        self.rawDataLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.transformDataLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

