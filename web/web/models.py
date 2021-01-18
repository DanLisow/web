from sqlalchemy import Column, Integer, Text, create_engine
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+mysqlconnector://root:root@localhost/pyramid?charset=utf8mb4")
Session = sessionmaker()
Base = declarative_base(bind=engine)


class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    text = Column(Text)

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __repr__(self):
        return "<Note('%s','%s')>" % (self.title, self.text)

# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     password = Column(String)

#     def __init__(self, name, password):
#         self.name = name
#         self.password = password

#     def __repr__(self):
#         return "<User('%s','%s')>" % (self.name, self.password)

Base.metadata.create_all(engine)