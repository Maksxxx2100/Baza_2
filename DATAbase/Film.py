from sqlalchemy import Column, Integer, String,Date
from sqlalchemy.orm import relationship

from base_meta import Base

class Film(Base):
    __tablename__ = "Film"

    film_id = Column(Integer, primary_key=True, autoincrement=True)
    film_title = Column(String(50), nullable=False)
    film_duration = Column(Integer)
    film_release_date = Column(Date)

    def __repr__(self):
        return f"Film(id={self.id!r}, title={self.film_title!r}, duration = {self.film_duration!r},date={self.film_release_date})"