# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(552, 300)
        Dialog.setMinimumSize(QtCore.QSize(552, 0))
        Dialog.setMaximumSize(QtCore.QSize(552, 16777215))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 110, 411, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.InputHorizantalPassword = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.InputHorizantalPassword.setContentsMargins(0, 0, 0, 0)
        self.InputHorizantalPassword.setObjectName("InputHorizantalPassword")
        self.sudoPasswordLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.sudoPasswordLabel.setObjectName("sudoPasswordLabel")
        self.InputHorizantalPassword.addWidget(self.sudoPasswordLabel)
        self.passwordInput = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.passwordInput.setObjectName("passwordInput")
        self.InputHorizantalPassword.addWidget(self.passwordInput)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.sudoPasswordLabel.setText(_translate("Dialog", "Sudo Password : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
