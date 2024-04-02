from sqlalchemy import Column, Integer, String,Date
from sqlalchemy.orm import relationship

from base_meta import Base

class Serial(Base):
    __tablename__ = "Serial"

    serial_id = Column(Integer, primary_key=True, autoincrement=True)
    serial_title = Column(String(50), nullable=False)
    serial_ep = Column(Integer)
    serial_release_date = Column(Date)
    category_id = relationship("Category", back_populates="serial")

    def __repr__(self):
        return f"Film(id={self.id!r}, title={self.film_title!r}, duration = {self.film_duration!r},date={self.film_release_date})"