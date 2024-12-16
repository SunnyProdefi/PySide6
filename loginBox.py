# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginBox.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(181, 149)
        self.label = QLabel(dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 54, 16))
        self.label_2 = QLabel(dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 54, 16))
        self.lineEdit = QLineEdit(dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 30, 113, 20))
        self.lineEdit_2 = QLineEdit(dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(60, 60, 113, 20))
        self.pushButton = QPushButton(dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 110, 75, 24))

        self.retranslateUi(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"\u767b\u5f55\u6846", None))
        self.label.setText(QCoreApplication.translate("dialog", u"\u8d26\u53f7", None))
        self.label_2.setText(QCoreApplication.translate("dialog", u"\u5bc6\u7801", None))
        self.lineEdit.setText(QCoreApplication.translate("dialog", u"\u8bf7\u8f93\u5165\u8d26\u53f7", None))
        self.lineEdit_2.setText(QCoreApplication.translate("dialog", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.pushButton.setText(QCoreApplication.translate("dialog", u"\u767b\u5f55", None))
    # retranslateUi

