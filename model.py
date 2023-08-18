import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("sqlite:///memory")
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

class Order_(Base):
    __tablename__ = 'order_'
    id = Column(Integer, primary_key=True)
    date_ = Column(DateTime)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    status_id = Column(Integer, ForeignKey('status.id'))
    customers = relationship('Customer', back_populates='orders')
    statuss = relationship('Status', back_populates='orders')
    products_orders = relationship('Product_order', back_populates='orders')



Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

