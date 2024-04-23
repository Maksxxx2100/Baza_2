from typing import Iterable, Callable
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from DATAbase import get_session, Film, Category, Film_Actor, Film_Filmmaker, Filmmaker
from ui import UiAdminFilmInfoForm
from .Admin_Actors_list import AdminActorsList
from sqlalchemy.sql import text


class AdminFilmInfo(QWidget, UiAdminFilmInfoForm):
    def __init__(self, film: Film, callbacks: Iterable[Callable]):
        super().__init__()
        self.setupUi(self)
        self.callbacks = callbacks
        self.create_window = None
        self.session = get_session()
        self.Just_Do_It_pushButton.clicked.connect(self.update_film)
        self.goto_actors_pushButton.clicked.connect(self.actors_list)
        self.close_pushButton.clicked.connect(lambda: self.close())
        self.film_id = int(film.film_id)


        self.title_lineEdit.setText(str(film.film_title))
        self.time_lineEdit.setText(str(film.film_duration))
        self.date_lineEdit.setText(str(film.film_release_date))
        film_fmaker = self.session.query(Film_Filmmaker).filter(Film_Filmmaker.film_id == self.film_id).all()
        for fmaker in film_fmaker:
            self.fmaker_lineEdit.setText(str(fmaker.fmaker.fmakers_name))
        self.category_lineEdit.setText(str(film.category.category_title))
        self.textEdit.setText('Много лет тому назад...')

    def update_film(self):
        title = self.title_lineEdit.text()
        time = self.time_lineEdit.text()
        category = self.category_lineEdit.text()
        date = self.date_lineEdit.text()
        fmaker = self.fmaker_lineEdit.text()
        film_id = self.film_id
        exist_film: Film = self.session.query(Film).get(film_id)
        exist_film_fmaker: Film_Filmmaker = self.session.query(Film_Filmmaker).filter(Film_Filmmaker.film_id == film_id).one()
        exist_fmaker: Filmmaker = self.session.query(Filmmaker).filter(Filmmaker.fmakers_name == fmaker).all()
        if len(exist_fmaker) == 0:
            self.session2 = get_session()
            new_fmaker = Filmmaker(fmakers_name=fmaker)
            self.session2.add(new_fmaker)
            self.session2.commit()
            self.session2.close()
            self.session2 = get_session()
            self.session2.delete(exist_film_fmaker)
            self.session2.commit()
            self.session2.close()
            self.session2 = get_session()
            added_fmaker: Filmmaker = self.session2.query(Filmmaker).filter(Filmmaker.fmakers_name == fmaker).all()
            new_film_fmaker = Film_Filmmaker(film_id=film_id, fmaker_id=added_fmaker.fmaker_id)
            self.session2.merge(new_film_fmaker)
            self.session2.commit()
            self.session2.close()
        else:
            self.session2 = get_session()
            exist_film_fmaker.fmaker_id = exist_fmaker[0].fmaker_id
            self.session2.commit()
            self.session2.close()
        exist_film.film_title = title
        exist_film.film_duration = time
        exist_film.category.category_title = category
        exist_film.film_release_date = date
        self.session.commit()
        self.custom_close()

    def actors_list(self):
        film_actor = self.session.query(Film_Actor).filter(Film_Actor.film_id == self.film_id).all()
        self.create_window = AdminActorsList(film_actor)
        for actor in film_actor:
            print(actor.film_id)
        self.create_window.show()

    def custom_close(self):
        for callback in self.callbacks:
            callback()
        self.close()