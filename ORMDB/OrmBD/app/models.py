from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from . import  db


class Good(Model):
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(30), nullable=False)
    size = db.Column(Integer, nullable=False)

    def __repr__(self):
        return self.name


class Customer(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    phone = Column(String(12), nullable=False)
    index = Column(String(8), nullable=False)
    def __repr__(self):
        return self.name


class Lead(Model):
    id = Column(Integer, primary_key=True)
    personid = Column(Integer, db.ForeignKey('customer.id'), nullable=True)
    date = Column(Date, default=func.now())
    price = Column(Integer)
    goodid = Column(Integer, db.ForeignKey('good.id'))
    cust_rel = relationship('Customer')
    good_rel = relationship('Good')


    def __repr__(self):
        return self.id


class Warehouse(Model):
    id = Column(Integer, primary_key=True)
    goodid = Column(Integer, ForeignKey('good.id'))
    admission_date = Column(Date)
    cost = Column(Integer)
    good_rel = relationship('Good')

    def __repr__(self):
        return self.id
