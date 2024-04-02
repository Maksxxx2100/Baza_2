from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from base_meta import Base

class Film_Filmmaker(Base):
    __tablename__ = "Film_Filmmaker"

    fmaker_id = Column(ForeignKey("Filmmaker.fmaker_id"), primary_key=True)
    film_id = Column(ForeignKey("Film.film_id"), primary_key=True)

    fmaker = relationship("Filmmaker", back_populates="fmaker_film")
    film = relationship("Film", back_populates="film_fmaker")

    def __repr__(self):
        return f"FilmFmaker(Film_id={self.film_id!r}, Filmmaker_id = {self.fmaker_id!r})"