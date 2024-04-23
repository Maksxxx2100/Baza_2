from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from DATAbase import get_session, Film, Category, Film_Actor, Actor
from ui import UiAdminActorslistForm
from sqlalchemy.sql import text
from .Admin_Actor_info import AdminActorInfo


class AdminActorsList(QWidget, UiAdminActorslistForm):
    def __init__(self, film_actor: Film_Actor):
        super().__init__()
        self.setupUi(self)
        self.session = get_session()
        self.back_pushButton.clicked.connect(lambda: self.close())

        self.tableWidget.cellDoubleClicked.connect(self.admin_actorInfo)
        self.film_actor = film_actor
        self.createTable()

    def createTable(self):
        actors = self.session.query(Film_Actor).filter(Film_Actor.film_id == self.film_actor[0].film_id).all()
        self.tableWidget.setRowCount(0)
        for actor in actors:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(str(actor.actor.actor_id)))
            self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(str(actor.actor.actors_name)))
            self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(str(actor.actor.actors_birth)))

    def admin_actorInfo(self, row, column):
        actor_id = int(self.tableWidget.item(row, 0).text())
        film = self.session.query(Film).get(self.film_actor[0].film_id)
        actor = self.session.query(Actor).get(actor_id)
        self.create_window = AdminActorInfo(actor, film, [self.createTable])
        self.create_window.show()

    def custom_close(self):
        for callback in self.callbacks:
            callback()
        self.close()