# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\user\PycharmProject\SMRPprjct\ui\from_designer\Admin_Film_Info.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Admin_Film_Info_Form(object):
    def setupUi(self, Admin_Film_Info_Form):
        Admin_Film_Info_Form.setObjectName("Admin_Film_Info_Form")
        Admin_Film_Info_Form.resize(660, 697)
        self.gridLayout = QtWidgets.QGridLayout(Admin_Film_Info_Form)
        self.gridLayout.setObjectName("gridLayout")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("логотип_приложения.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Admin_Film_Info_Form.setWindowIcon(icon)
        self.label_4 = QtWidgets.QLabel(Admin_Film_Info_Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(Admin_Film_Info_Form)
        self.textEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 4, 1, 1, 1)
        self.date_lineEdit = QtWidgets.QLineEdit(Admin_Film_Info_Form)
        self.date_lineEdit.setObjectName("date_lineEdit")
        self.gridLayout.addWidget(self.date_lineEdit, 5, 1, 1, 1)
        self.time_lineEdit = QtWidgets.QLineEdit(Admin_Film_Info_Form)
        self.time_lineEdit.setObjectName("time_lineEdit")
        self.gridLayout.addWidget(self.time_lineEdit, 3, 1, 1, 1)
        self.fmaker_lineEdit = QtWidgets.QLineEdit(Admin_Film_Info_Form)
        self.fmaker_lineEdit.setObjectName("fmaker_lineEdit")
        self.gridLayout.addWidget(self.fmaker_lineEdit, 6, 1, 1, 1)
        self.close_pushButton = QtWidgets.QPushButton(Admin_Film_Info_Form)
        self.close_pushButton.setObjectName("close_pushButton")
        self.gridLayout.addWidget(self.close_pushButton, 8, 0, 1, 1)
        self.title_lineEdit = QtWidgets.QLineEdit(Admin_Film_Info_Form)
        self.title_lineEdit.setObjectName("title_lineEdit")
        self.gridLayout.addWidget(self.title_lineEdit, 0, 1, 1, 1)
        self.category_lineEdit = QtWidgets.QLineEdit(Admin_Film_Info_Form)
        self.category_lineEdit.setObjectName("category_lineEdit")
        self.gridLayout.addWidget(self.category_lineEdit, 1, 1, 2, 1)
        self.label_5 = QtWidgets.QLabel(Admin_Film_Info_Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Admin_Film_Info_Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Admin_Film_Info_Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Admin_Film_Info_Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.goto_actors_pushButton = QtWidgets.QPushButton(Admin_Film_Info_Form)
        self.goto_actors_pushButton.setObjectName("goto_actors_pushButton")
        self.gridLayout.addWidget(self.goto_actors_pushButton, 7, 1, 1, 1)
        self.label = QtWidgets.QLabel(Admin_Film_Info_Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 2, 1)
        self.Just_Do_It_pushButton = QtWidgets.QPushButton(Admin_Film_Info_Form)
        self.Just_Do_It_pushButton.setObjectName("Just_Do_It_pushButton")
        self.gridLayout.addWidget(self.Just_Do_It_pushButton, 8, 1, 1, 1)

        self.retranslateUi(Admin_Film_Info_Form)
        QtCore.QMetaObject.connectSlotsByName(Admin_Film_Info_Form)

    def retranslateUi(self, Admin_Film_Info_Form):
        _translate = QtCore.QCoreApplication.translate
        Admin_Film_Info_Form.setWindowTitle(_translate("Film_list", "KinoSearch"))
        self.label_4.setText(_translate("Admin_Film_Info_Form", "Краткое описание:"))
        self.close_pushButton.setText(_translate("Admin_Film_Info_Form", "Закрыть"))
        self.label_5.setText(_translate("Admin_Film_Info_Form", "Год выпуска:"))
        self.label_3.setText(_translate("Admin_Film_Info_Form", "Время:"))
        self.label_6.setText(_translate("Admin_Film_Info_Form", "Режиссер:"))
        self.label_2.setText(_translate("Admin_Film_Info_Form", "Жанр:"))
        self.goto_actors_pushButton.setText(_translate("Admin_Film_Info_Form", "Актеры"))
        self.label.setText(_translate("Admin_Film_Info_Form", "Название:"))
        self.Just_Do_It_pushButton.setText(_translate("Admin_Film_Info_Form", "Применить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admin_Film_Info_Form = QtWidgets.QWidget()
    ui = Ui_Admin_Film_Info_Form()
    ui.setupUi(Admin_Film_Info_Form)
    Admin_Film_Info_Form.show()
    sys.exit(app.exec_())
