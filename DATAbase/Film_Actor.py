from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from base_meta import Base

class Film_Actor(Base):
    __tablename__ = "Film_Actor"

    actor_id = Column(ForeignKey("Actor.actor_id"), primary_key=True)
    film_id = Column(ForeignKey("Film.film_id"), primary_key=True)

    actor = relationship("Actor", back_populates="actor_film")
    film = relationship("Film", back_populates="film_actor")

