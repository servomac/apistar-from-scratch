from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()

class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    definition = Column(String(128))
    completed = Column(Boolean, default=False)

    def __repr__(self):
        return '<Task id={}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'definition': self.definition,
            'completed': self.completed,
        }
