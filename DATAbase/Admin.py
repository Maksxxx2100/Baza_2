from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base_meta import Base

class Admin(Base):
    __tablename__ = "Admin"

    admin_id = Column(Integer, primary_key=True, autoincrement=True)
    admin_login = Column(String(50), nullable=False)
    admin_password = Column(String(50))


    def __repr__(self):
        return f"Admin(id={self.admin_id!r}, login={self.admin_login!r}, password = {self.admin_password!r})"