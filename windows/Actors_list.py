from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from DATAbase import get_session, Film, Category, Film_Actor, Actor
from ui import UiActorsListForm
from sqlalchemy.sql import text


class ActorsList(QWidget, UiActorsListForm):
    def __init__(self, film_actor: Film_Actor):
        super().__init__()
        self.setupUi(self)
        self.session = get_session()
        self.back_pushButton.clicked.connect(lambda: self.close())
        self.createTable(film_actor)

    def createTable(self, film_actor):
        self.tableWidget.setRowCount(0)
        for actor in film_actor:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(actor.actor.actor_id)))
            self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(str(actor.actor.actors_name)))
            self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(str(actor.actor.actors_birth)))

