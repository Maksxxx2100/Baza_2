from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base

class Serial_Filmmaker(Base):
    __tablename__ = "Serial_Filmmaker"

    fmaker_id = Column(ForeignKey("Filmmaker.fmaker_id"), primary_key=True)
    serial_id = Column(ForeignKey("Serial.serial_id"), primary_key=True)

    fmaker = relationship("Filmmaker", back_populates="fmaker_serial")
    serial = relationship("Serial", back_populates="serial_fmaker")

    def __repr__(self):
        return f"SerialFmaker(Serial_id={self.serial_id!r}, Filmmaker_id = {self.fmaker_id!r})"