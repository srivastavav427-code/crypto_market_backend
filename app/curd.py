from sqlalchemy.orm import Session
from . import models

def get_market(db: Session, symbol: str):
    return db.query(models.Market).filter(models.Market.symbol == symbol).first()

def create_or_update_market(db: Session, symbol: str, price: float):
    market = get_market(db, symbol)
    if market:
        market.current_price = price
    else:
        market = models.Market(symbol=symbol, current_price=price)
        db.add(market)
    db.commit()
    db.refresh(market)
    return market
