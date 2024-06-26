from typing import Iterable, Callable

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from DATAbase import get_session, Film, Category
from ui import UiAdminFilmListForm
from .Admin_Film_info import AdminFilmInfo
from sqlalchemy.sql import text


class AdminFilmList(QWidget, UiAdminFilmListForm):
    def __init__(self):
        super().__init__()
        #self.callbacks = callbacks
        self.create_window = None
        self.setupUi(self)
        self.Film_tableWidget.cellDoubleClicked.connect(self.admin_filmInfo)
        self.session = get_session()
        self.gosearch_pushButton.clicked.connect(self.updateTable)
        self.backto_choose_pushButton.clicked.connect(lambda: self.close())
        #self.Film_tableWidget.cellDoubleClicked.connect(self.filmInfo)
        categories = self.session.query(Category).all()
        self.category_comboBox.addItem('*')
        for category in categories:
            self.category_comboBox.addItem(category.category_title)
        self.category_comboBox.activated.connect(self.goFiltr)

        self.createTable()


    def createTable(self):
        films = self.session.query(Film).order_by(Film.film_id).all()
        self.Film_tableWidget.setRowCount(0)
        for film in films:
            rowPosition = self.Film_tableWidget.rowCount()
            self.Film_tableWidget.insertRow(rowPosition)
            self.Film_tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(film.film_id)))
            self.Film_tableWidget.setItem(rowPosition, 1, QTableWidgetItem(str(film.film_title)))
            self.Film_tableWidget.setItem(rowPosition, 2, QTableWidgetItem(str(film.category.category_title)))
            self.Film_tableWidget.setItem(rowPosition, 3, QTableWidgetItem(str(film.film_duration)))
            self.Film_tableWidget.setItem(rowPosition, 4, QTableWidgetItem(str(film.film_release_date)))


    def updateTable(self, category_set):
        request = self.search_lineEdit.text()
        if category_set == 0:
            films = self.session.query(Film).order_by(Film.film_id).all()
        else:
            films = self.session.query(Film).filter(Film.category_id == category_set).order_by(Film.film_id).all()
        self.Film_tableWidget.setRowCount(0)
        for film in films:
            if request.lower() in str(film.film_title).lower()[:len(request)-len(film.film_title)]:
                self.filling_table(film)
            else: continue


    def filling_table(self, film):
        rowPosition = self.Film_tableWidget.rowCount()
        self.Film_tableWidget.insertRow(rowPosition)
        self.Film_tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(film.film_id)))
        self.Film_tableWidget.setItem(rowPosition, 1, QTableWidgetItem(str(film.film_title)))
        self.Film_tableWidget.setItem(rowPosition, 2, QTableWidgetItem(str(film.category.category_title)))
        self.Film_tableWidget.setItem(rowPosition, 3, QTableWidgetItem(str(film.film_duration)))
        self.Film_tableWidget.setItem(rowPosition, 4, QTableWidgetItem(str(film.film_release_date)))


    def goFiltr(self):
        if self.category_comboBox.currentText() == '*':
            category_set = 0
        else:
            categories = self.session.query(Category).filter(Category.category_title == str(self.category_comboBox.currentText())).all()
            category_set = categories[0].category_id
        self.updateTable(category_set)


    def admin_filmInfo(self, row, column):
        film_id = int(self.Film_tableWidget.item(row, 0).text())
        film = self.session.query(Film).get(film_id)
        self.create_window = AdminFilmInfo(film, [self.createTable])
        self.create_window.show()


    def custom_close(self):
        for callback in self.callbacks:
            callback()
        self.close()