from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from core.db import Base
from user.models import User


class Post(Base):
    __tablename__ = "microblog posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    text = Column(String(350))
    date = Column(DateTime)
    user = Column(Integer, ForeignKey("user.id"))
    user_id = relationship(User)

