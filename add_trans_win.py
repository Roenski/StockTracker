# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiAddT.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1200, 200))
        Form.setSizeIncrement(QtCore.QSize(10, 10))
        Form.setBaseSize(QtCore.QSize(0, 0))
        self.verticalLayoutWidget_13 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(10, 30, 1151, 141))
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.edit_tDate = QtWidgets.QDateEdit(self.verticalLayoutWidget_13)
        self.edit_tDate.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.edit_tDate.setObjectName("edit_tDate")
        self.verticalLayout_7.addWidget(self.edit_tDate)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.label_2)
        self.combo_tType = QtWidgets.QComboBox(self.verticalLayoutWidget_13)
        self.combo_tType.setObjectName("combo_tType")
        self.verticalLayout_9.addWidget(self.combo_tType)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_10.addWidget(self.label_3)
        self.combo_tBS = QtWidgets.QComboBox(self.verticalLayoutWidget_13)
        self.combo_tBS.setObjectName("combo_tBS")
        self.verticalLayout_10.addWidget(self.combo_tBS)
        self.horizontalLayout_3.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_11.addWidget(self.label_4)
        self.combo_sName = QtWidgets.QComboBox(self.verticalLayoutWidget_13)
        self.combo_sName.setObjectName("combo_sName")
        self.verticalLayout_11.addWidget(self.combo_sName)
        self.horizontalLayout_3.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_12.addWidget(self.label_5)
        self.line_sQuantity = QtWidgets.QLineEdit(self.verticalLayoutWidget_13)
        self.line_sQuantity.setToolTip("")
        self.line_sQuantity.setStatusTip("")
        self.line_sQuantity.setInputMask("")
        self.line_sQuantity.setText("")
        self.line_sQuantity.setObjectName("line_sQuantity")
        self.verticalLayout_12.addWidget(self.line_sQuantity)
        self.horizontalLayout_3.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_13.addWidget(self.label_6)
        self.line_sPrice = QtWidgets.QLineEdit(self.verticalLayoutWidget_13)
        self.line_sPrice.setObjectName("line_sPrice")
        self.verticalLayout_13.addWidget(self.line_sPrice)
        self.horizontalLayout_3.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_14.addWidget(self.label_7)
        self.combo_sPriceCurrency = QtWidgets.QComboBox(self.verticalLayoutWidget_13)
        self.combo_sPriceCurrency.setObjectName("combo_sPriceCurrency")
        self.verticalLayout_14.addWidget(self.combo_sPriceCurrency)
        self.horizontalLayout_3.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_15.addWidget(self.label_8)
        self.line_sPriceExchange = QtWidgets.QLineEdit(self.verticalLayoutWidget_13)
        self.line_sPriceExchange.setObjectName("line_sPriceExchange")
        self.verticalLayout_15.addWidget(self.line_sPriceExchange)
        self.horizontalLayout_3.addLayout(self.verticalLayout_15)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_16.addWidget(self.label_9)
        self.line_sFee = QtWidgets.QLineEdit(self.verticalLayoutWidget_13)
        self.line_sFee.setObjectName("line_sFee")
        self.verticalLayout_16.addWidget(self.line_sFee)
        self.horizontalLayout_3.addLayout(self.verticalLayout_16)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_12.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_22.addWidget(self.label_12)
        self.combo_sFeeCurrency = QtWidgets.QComboBox(self.verticalLayoutWidget_13)
        self.combo_sFeeCurrency.setObjectName("combo_sFeeCurrency")
        self.verticalLayout_22.addWidget(self.combo_sFeeCurrency)
        self.horizontalLayout_3.addLayout(self.verticalLayout_22)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_11.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_21.addWidget(self.label_11)
        self.line_sFeeExchange = QtWidgets.QLineEdit(self.verticalLayoutWidget_13)
        self.line_sFeeExchange.setObjectName("line_sFeeExchange")
        self.verticalLayout_21.addWidget(self.line_sFeeExchange)
        self.horizontalLayout_3.addLayout(self.verticalLayout_21)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_10.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_8.addWidget(self.label_10)
        self.combo_tBroker = QtWidgets.QComboBox(self.verticalLayoutWidget_13)
        self.combo_tBroker.setObjectName("combo_tBroker")
        self.verticalLayout_8.addWidget(self.combo_tBroker)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(800, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_add = QtWidgets.QPushButton(self.verticalLayoutWidget_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout.addWidget(self.pushButton_add)
        self.pushButton_cancel = QtWidgets.QPushButton(self.verticalLayoutWidget_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cancel.sizePolicy().hasHeightForWidth())
        self.pushButton_cancel.setSizePolicy(sizePolicy)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Date"))
        self.label_2.setText(_translate("Form", "Type"))
        self.label_3.setText(_translate("Form", "Buy/Sell"))
        self.label_4.setText(_translate("Form", "Name"))
        self.label_5.setText(_translate("Form", "Quantity"))
        self.line_sQuantity.setPlaceholderText(_translate("Form", "Quantity"))
        self.label_6.setText(_translate("Form", "Price per stock"))
        self.line_sPrice.setPlaceholderText(_translate("Form", "Price"))
        self.label_7.setText(_translate("Form", "Currency"))
        self.label_8.setText(_translate("Form", "Exchange rate"))
        self.line_sPriceExchange.setPlaceholderText(_translate("Form", "Exchange"))
        self.label_9.setText(_translate("Form", "Fee"))
        self.line_sFee.setPlaceholderText(_translate("Form", "Fee"))
        self.label_12.setText(_translate("Form", "Fee Currency"))
        self.label_11.setText(_translate("Form", "Fee Exchange rate"))
        self.line_sFeeExchange.setPlaceholderText(_translate("Form", "Fee Exchange"))
        self.label_10.setText(_translate("Form", "Broker"))
        self.pushButton_add.setText(_translate("Form", "Add"))
        self.pushButton_cancel.setText(_translate("Form", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
