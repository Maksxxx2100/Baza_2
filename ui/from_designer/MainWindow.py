# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from DATAbase import User,Admin  # для дополнения в базу данных пользователей
from DATAbase import get_session
from Window_reg import Ui_Form
from Menuu import Ui_Form_2

from PyQt5.QtWidgets import QMessageBox

session = get_session()
#session.query(User).delete()  # отчистка всего
#session.commit()

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def open_reg(self):  # открытие 2 окна
        self.window2 = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def open_menu(self,a):  # открытие окна меню
        self.window3 = QtWidgets.QWidget()
        self.ui = Ui_Form_2(a)
        #self.ui.user_check = a
        self.ui.setupUi(self.window3)
        self.window3.show()



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(534, 279)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("логотип_приложения.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2") # кнопка ок
        self.gridLayout.addWidget(self.pushButton_2, 7, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 5, 2, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 6, 2, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton") # кнопка регистрации
        self.gridLayout.addWidget(self.pushButton, 7, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def open_window(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        user_check = session.query(User).filter(User.login == login).all()  # ищем юзера по нику
        admin_check = session.query(Admin).filter(Admin.admin_login == login).all()  # ищем admina по нику
        print("lkbyf: ",len(admin_check))
        if(len(user_check)!=0 and len(admin_check)==0):
            if(user_check[0].password == password):
                MainWindow.close()
                self.open_menu(0)
                print("добро пожаловать")
            else:
                error = QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("неправильный логин или пароль")   # всплывающее окно
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok)
                error.exec_()
                print("неправильный логин или пароль")
        else:
            if(len(admin_check)==0):
                error = QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("неправильный логин или пароль")  # всплывающее окно
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok)
                error.exec_()
                print("неправильный логин или пароль")
            else:
                if(admin_check[0].admin_password == password):
                    MainWindow.close()
                    print("Добро пожаловать, создатель")
                    self.open_menu(1)




    def add_functions(self):
        self.pushButton.clicked.connect(self.open_reg)  # reg
        self.pushButton_2.clicked.connect(self.open_window) #next



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KinoSearch"))
        self.label_4.setText(_translate("MainWindow", "Пароль:"))
        self.label_2.setText(_translate("MainWindow", "Войдите или зрегистрируйтесь "))
        self.pushButton_2.setText(_translate("MainWindow", "Ок"))
        self.label_3.setText(_translate("MainWindow", "Логин: "))
        self.label.setText(_translate("MainWindow", "KinoSearch"))
        self.pushButton.setText(_translate("MainWindow", "Регистрация"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
