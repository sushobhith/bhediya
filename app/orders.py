from fastapi import APIRouter
from kiteconnect import KiteConnect
from .auth import kite

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/place")
def place_order(order: dict):
    """
    Example order dict:
    {
      "exchange":"NSE","tradingsymbol":"INFY","transaction_type":"BUY",
      "quantity":10,"order_type":"MARKET","product":"MIS","validity":"DAY"
    }
    """
    return kite.place_order(variety="regular", **order)

@router.put("/modify/{order_id}")
def modify_order(order_id: str, fields: dict):
    return kite.modify_order(order_id=order_id, **fields)

@router.delete("/cancel/{order_id}")
def cancel_order(order_id: str):
    return kite.cancel_order(order_id=order_id)

@router.get("/")
def list_orders():
    return kite.orders()

@router.get("/trades")
def list_trades():
    return kite.trades()
