from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from base_meta import Base

class Film_Review(Base):
    __tablename__ = "Film_Review"

    film_id = Column(ForeignKey("Film.film_id"), primary_key=True)
    review_id = Column(ForeignKey("Review.review_id"), primary_key=True)

    film = relationship("Film", back_populates="film_review")
    review = relationship("Review", back_populates="review_film")

    def __repr__(self):
        return f"FilmReview(Film_id={self.film_id!r}, Review_id = {self.review_id!r})"