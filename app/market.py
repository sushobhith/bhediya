from fastapi import APIRouter, Depends
from kiteconnect import KiteConnect
from .auth import kite

router = APIRouter(prefix="/market", tags=["market"])

@router.get("/instruments")
def get_instruments():
    return kite.instruments()

@router.get("/quote")
def get_quote(exchange: str, symbol: str):
    key = f"{exchange}:{symbol}"
    return kite.quote(key)

@router.get("/historical")
def get_historical(instrument_token: int, from_date: str, to_date: str, interval: str):
    # dates as "YYYY-MM-DD"
    return kite.historical_data(
        instrument_token=int(instrument_token),
        from_date=from_date,
        to_date=to_date,
        interval=interval
    )
