from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from base_meta import Base

class Category(Base):
    __tablename__ = "Category"

    category_id = Column(Integer, primary_key=True, autoincrement=True)
    category_title = Column(String(50), nullable=False)

    def __repr__(self):
        return f"Category(id={self.id!r}, title={self.category_title!r})"