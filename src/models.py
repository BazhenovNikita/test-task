from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, DeclarativeBase


class Base(DeclarativeBase):
    ...


class QueueRequests(Base):
    __tablename__ = 'queue_requests'
    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    method = Column(String, nullable=False)
    params = Column(String)
    headers = Column(String)
    processed = Column(Boolean, default=True)
    queue_response = relationship('QueueResponses', backref='queue_requests', uselist=False)


class QueueResponses(Base):
    __tablename__ = 'queue_responses'
    id = Column(Integer, primary_key=True)
    request_id = Column(Integer, ForeignKey('queue_requests.id'))
    status_code = Column(Integer, nullable=False)
    body = Column(String)
