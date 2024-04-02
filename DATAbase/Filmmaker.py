from sqlalchemy import Column, Integer, String,Date
from sqlalchemy.orm import relationship

from base_meta import Base

class Filmmaker(Base):
    __tablename__ = "Filmmaker"

    fmaker_id = Column(Integer, primary_key=True, autoincrement=True)
    fmakers_name = Column(String(50), nullable=False)
    fmakers_birth = Column(Date)

    def __repr__(self):
        return f"Filmmaker(id={self.fmaker_id!r}, name={self.fmakers_name!r}, birth = {self.fmakers_birth!r})"