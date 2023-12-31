

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String(30))
    userename = Column(String(30))
    created = Column('created_on', DateTime, default=datetime.now)
    updated = Column('last_updated', DateTime, onupdate=datetime.now)
    is_active = Column(Boolean, default=True)
    items = relationship("Item", back_populates="owner",cascade='all, delete')


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")



    