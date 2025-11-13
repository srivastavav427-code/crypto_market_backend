from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from decimal import Decimal
from datetime import datetime

from pydantic import BaseModel

class MarketBase(BaseModel):
    name: str
    symbol: str
    base_currency: str
    quote_currency: str

class MarketCreate(MarketBase):
    pass  # used when creating a new market

class Market(MarketBase):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    balance: Decimal

    class Config:
        orm_mode = True

class MarketIn(BaseModel):
    symbol: str
    price: Decimal

class MarketOut(BaseModel):
    id: int
    symbol: str
    current_price: Decimal
    class Config:
        orm_mode = True

class TradeIn(BaseModel):
    user_id: int
    symbol: str
    type: str  # buy or sell
    price: Decimal
    quantity: Decimal

class AlertIn(BaseModel):
    user_id: int
    symbol: str
    direction: str
    target_price: Decimal

class HoldingOut(BaseModel):
    symbol: str
    quantity: Decimal
    avg_buy_price: Decimal
    current_price: Decimal
    unrealized_pnl: Decimal

class PortfolioOut(BaseModel):
    balance: Decimal
    holdings: List[HoldingOut]
    total_value: Decimal