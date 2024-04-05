from sqlalchemy import Column, Integer, String,Date
from sqlalchemy.orm import relationship

from .base_meta import Base

class User(Base):
    __tablename__ = "User"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    #story_list
    #grades_list
    user_review = relationship("User_Review", back_populates="user")
    user_film = relationship("User_Film", back_populates="user")
    user_serial = relationship("User_Serial", back_populates="user")

    def __repr__(self):
        return f"User(id={self.user_id!r}, login={self.login!r}, password = {self.password!r})"
