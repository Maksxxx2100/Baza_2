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
    serial_actor = relationship("Serial_Actor", back_populates="serial")
    serial_fmaker = relationship("Serial_Filmmaker", back_populates="serial")
    serial_review = relationship("Serial_Review", back_populates="serial")
    serial_user = relationship("User_Serial", back_populates="serial")

    def __repr__(self):
        return f"Serial(id={self.serial_id!r}, title={self.serial_title!r}, duration = {self.serial_ep!r},date={self.serial_release_date!r})"