from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base

class Serial_Actor(Base):
    __tablename__ = "Serial_Actor"

    actor_id = Column(ForeignKey("Actor.actor_id"), primary_key=True)
    serial_id = Column(ForeignKey("Serial.serial_id"), primary_key=True)

    actor = relationship("Actor", back_populates="actor_serial")
    serial = relationship("Serial", back_populates="serial_actor")

    def __repr__(self):
        return f"SerialActor(Serial_id={self.serial_id!r}, Actor_id = {self.actor_id!r})"