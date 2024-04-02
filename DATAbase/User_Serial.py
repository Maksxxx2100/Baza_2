from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from base_meta import Base

class User_Serial(Base):
    __tablename__ = "User_Serial"

    user_id = Column(ForeignKey("User.user_id"), primary_key=True)
    serial_id = Column(ForeignKey("Serial.serial_id"), primary_key=True)

    user = relationship("User", back_populates="user_serial")
    serial = relationship("Serial", back_populates="serial_user")

    def __repr__(self):
        return f"UserSerial(User_id={self.user_id!r}, Serial_id = {self.serial_id!r})"