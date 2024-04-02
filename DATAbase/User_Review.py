from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from base_meta import Base

class User_Review(Base):
    __tablename__ = "User_Review"

    user_id = Column(ForeignKey("User.user_id"), primary_key=True)
    review_id = Column(ForeignKey("Review.review_id"), primary_key=True)

    user = relationship("User", back_populates="user_review")
    review = relationship("Review", back_populates="review_user")

    def __repr__(self):
        return f"UserReview(User_id={self.user_id!r}, Review_id = {self.review_id!r})"


