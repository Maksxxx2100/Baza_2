from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from DATAbase import get_session, Film, Category, Film_Actor, Film_Filmmaker
from ui import UiFilmInfoForm
from .Actors_list import ActorsList
from sqlalchemy.sql import text


class FilmInfo(QWidget, UiFilmInfoForm):
    def __init__(self, film: Film):
        super().__init__()
        self.setupUi(self)
        self.create_window = None
        self.session = get_session()
        self.goto_actors_pushButton.clicked.connect(self.actors_list)
        self.close_pushButton.clicked.connect(lambda: self.close())
        self.film_id = int(film.film_id)


        self.title_label.setText(str(film.film_title))
        self.date_label.setText(str(film.film_duration))
        self.label_7.setText(str(film.film_release_date))
        film_fmaker = self.session.query(Film_Filmmaker).filter(Film_Filmmaker.film_id == self.film_id).all()
        for fmaker in film_fmaker:
            self.label_8.setText(str(fmaker.fmaker.fmakers_name))
        self.category_label.setText(str(film.category.category_title))
        self.textEdit.setText('Много лет тому назад...')

    def actors_list(self):
        film_actor = self.session.query(Film_Actor).filter(Film_Actor.film_id == self.film_id).all()
        self.create_window = ActorsList(film_actor)
        self.create_window.show()