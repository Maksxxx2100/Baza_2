from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from base_meta import Base

class Serial_Review(Base):
    __tablename__ = "Serial_Review"

    serial_id = Column(ForeignKey("Serial.Serial_id"), primary_key=True)
    review_id = Column(ForeignKey("Review.review_id"), primary_key=True)

    serial = relationship("Serial", back_populates="serial_review")
    review = relationship("Review", back_populates="review_serial")

    def __repr__(self):
        return f"SerialReview(Serial_id={self.serial_id!r}, Review_id = {self.review_id!r})"