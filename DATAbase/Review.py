from sqlalchemy import Column, Integer, String,Date
from sqlalchemy.orm import relationship

from .base_meta import Base

class Review(Base):
    __tablename__ = "Review"

    review_id = Column(Integer, primary_key=True, autoincrement=True)
    review_text = Column(String(255))
    review_grade = Column(Integer, nullable=False)

    review_user = relationship("User_Review", back_populates="review")
    review_film = relationship("Film_Review", back_populates="review")
    review_serial = relationship("Serial_Review", back_populates="review")

    def __repr__(self):
        return f"Review(id={self.review_id!r}, text={self.review_text!r}, grade = {self.review_grade!r})"