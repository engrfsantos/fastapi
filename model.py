from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base
  
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer,primary_key=True, nullable=False)
    title = Column(String, nullable=True)
    content = Column(String, nullable=True)
    published = Column(Boolean, nullable=True, Default=True)
    rate = Column(Integer,nullable=True)
    post_date = Column(DateTime, nullable=False, Default='Now()')
    
