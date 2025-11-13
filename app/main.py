from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from . import models, crud, schemas
from apscheduler.schedulers.background import BackgroundScheduler
import random

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "🚀 Crypto Market Backend is running!"}


app = FastAPI(title="Crypto Market Tracker")

Base.metadata.create_all(bind=engine)

@app.post("/api/markets/", response_model=schemas.MarketCreate)
def create_market(data: schemas.MarketCreate, db: Session = Depends(get_db)):
    return crud.create_or_update_market(db, data.symbol, data.price)

# Background price simulation
def simulate_prices():
    db = next(get_db())
    markets = db.query(models.Market).all()
    for m in markets:
        change = random.uniform(-100, 100)
        m.current_price = max(100, m.current_price + change)
    db.commit()
    print("✅ Prices updated")

scheduler = BackgroundScheduler()
scheduler.add_job(simulate_prices, "interval", seconds=5)
scheduler.start()

@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown()
