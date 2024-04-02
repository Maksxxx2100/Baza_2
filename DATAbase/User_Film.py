from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from base_meta import Base

class User_Film(Base):
    __tablename__ = "User_Film"

    user_id = Column(ForeignKey("User.user_id"), primary_key=True)
    film_id = Column(ForeignKey("Film.film_id"), primary_key=True)

    user = relationship("User", back_populates="user_film")
    film = relationship("Film", back_populates="film_user")

    def __repr__(self):
        return f"UserFilm(User_id={self.user_id!r}, Film_id = {self.film_id!r})"