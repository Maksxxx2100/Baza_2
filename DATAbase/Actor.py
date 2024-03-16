from sqlalchemy import Column, Integer, String,Date
from sqlalchemy.orm import relationship

from base_meta import Base

class Actor(Base):
    __tablename__ = "Actor"

    actor_id = Column(Integer, primary_key=True, autoincrement=True)
    actors_name = Column(String(50), nullable=False)
    actors_birth = Column(Date)

    def __repr__(self):
        return f"Film(id={self.id!r}, name={self.actors_name!r}, birth = {self.actors_birth!r})"