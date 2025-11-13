from sqlalchemy import Column, Integer, String, Numeric, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from decimal import Decimal
from sqlalchemy.types import TypeDecorator
import datetime

# Decimal type for SQLAlchemy (Numeric wrapper)
class DecimalType(TypeDecorator):
    impl = Numeric(precision=28, scale=10)

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        if isinstance(value, Decimal):
            return value
        return Decimal(str(value))

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        return Decimal(value)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    balance = Column(DecimalType, default=Decimal('10000'))

    holdings = relationship('Holding', back_populates='user')
    alerts = relationship('Alert', back_populates='user')
    transactions = relationship('TransactionLog', back_populates='user')

class Market(Base):
    __tablename__ = 'markets'
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True, nullable=False)
    current_price = Column(DecimalType, nullable=False)

    holdings = relationship('Holding', back_populates='market')
    alerts = relationship('Alert', back_populates='market')
    transactions = relationship('TransactionLog', back_populates='market')

class Holding(Base):
    __tablename__ = 'holdings'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    market_id = Column(Integer, ForeignKey('markets.id'))
    quantity = Column(DecimalType, default=Decimal('0'))
    avg_buy_price = Column(DecimalType, default=Decimal('0'))

    user = relationship('User', back_populates='holdings')
    market = relationship('Market', back_populates='holdings')

class Alert(Base):
    __tablename__ = 'alerts'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    market_id = Column(Integer, ForeignKey('markets.id'))
    target_price = Column(DecimalType, nullable=False)
    direction = Column(String, nullable=False)  # 'above' or 'below'
    triggered = Column(Boolean, default=False)

    user = relationship('User', back_populates='alerts')
    market = relationship('Market', back_populates='alerts')

class TransactionLog(Base):
    __tablename__ = 'transaction_logs'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    market_id = Column(Integer, ForeignKey('markets.id'))
    type = Column(String, nullable=False)  # 'buy' or 'sell'
    price = Column(DecimalType, nullable=False)
    quantity = Column(DecimalType, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship('User', back_populates='transactions')
    market = relationship('Market', back_populates='transactions')