from typing import Iterable, Callable
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from DATAbase import get_session, Film, Category, Film_Actor, Film_Filmmaker, Filmmaker, Actor
from ui import UiAdminActorInfoForm

from sqlalchemy.sql import text


class AdminActorInfo(QWidget, UiAdminActorInfoForm):
    def __init__(self, actor: Actor, film: Film, callbacks: Iterable[Callable]):
        super().__init__()
        self.setupUi(self)
        self.callbacks = callbacks
        self.create_window = None
        self.session = get_session()
        self.actor_id = int(actor.actor_id)
        self.film_id = int(film.film_id)
        actor = self.session.query(Actor).get(actor.actor_id)
        self.actors_name_lineEdit.setText(str(actor.actors_name))
        self.actors_bdate_lineEdit.setText(str(actor.actors_birth))
        self.Just_Do_It_pushButton.clicked.connect(self.update_actor)


    def update_actor(self):
        name = self.actors_name_lineEdit.text()
        bdate = self.actors_bdate_lineEdit.text()
        actor_id = self.actor_id
        film_id = self.film_id
        print(actor_id)
        #exist_film: Film = self.session.query(Film).get(film_id)
        exist_film_actor: Film_Actor = self.session.query(Film_Actor).filter(Film_Actor.film_id == film_id, Film_Actor.actor_id == actor_id).one()
        print(exist_film_actor)
        exist_actor: Actor = self.session.query(Actor).filter(Actor.actors_name == name).all()
        print(exist_actor)
        if len(exist_actor) == 0:
            self.session2 = get_session()
            new_actor = Actor(actors_name=name, actors_birth=bdate)
            print(new_actor)
            self.session2.add(new_actor)
            self.session2.commit()
            self.session2.close()
            self.session2 = get_session()
            self.session2.delete(exist_film_actor)
            self.session2.commit()
            self.session2.close()
            self.session2 = get_session()
            added_actor: Actor = self.session.query(Actor).filter(Actor.actors_name == name).all()
            print(added_actor)
            new_film_actor = Film_Actor(film_id=film_id, actor_id=added_actor.actor_id)
            self.session2.merge(new_film_actor)
            self.session2.commit()
            self.session2.close()
        else:
            self.session2 = get_session()
            exist_film_actor.actor_id = exist_actor[0].actor_id
            self.session2.commit()
            self.session2.close()
        """exist_actor.actors_name = name
        exist_actor.actors_birth = bdate"""
        self.session.commit()
        self.custom_close()

    def custom_close(self):
        for callback in self.callbacks:
            callback()
        self.close()