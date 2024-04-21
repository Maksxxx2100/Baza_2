from sqlalchemy import Column, Integer, String,Date,ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base

class Film(Base):
    __tablename__ = "Film"

    film_id = Column(Integer, primary_key=True, autoincrement=True)
    film_title = Column(String(50), nullable=False)
    film_duration = Column(Integer)
    film_release_date = Column(String(10))
    category = relationship("Category", back_populates="film")
    category_id = Column(ForeignKey("Category.category_id"), primary_key=True)
    film_actor = relationship("Film_Actor", back_populates="film")
    film_fmaker = relationship("Film_Filmmaker", back_populates="film")
    film_review = relationship("Film_Review", back_populates="film")
    film_user = relationship("User_Film", back_populates="film")

    def __repr__(self):
        return f"Film(id={self.film_id!r}, title={self.film_title!r}, duration = {self.film_duration!r},date={self.film_release_date!r})"