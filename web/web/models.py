from sqlalchemy import Column, Integer, Text, create_engine
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    "mysql+mysqlconnector://root:root@localhost/pyramid?charset=utf8mb4")
Session = sessionmaker()
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Text)

    def __repr__(self):
        return self.name
