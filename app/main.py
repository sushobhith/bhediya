from fastapi import FastAPI
from app.auth import router as auth_router
from app.market import router as market_router
from app.orders import router as orders_router

APP_VERSION = "0.1.0"

app = FastAPI(title="KiteConnect Intraday Service")

app.include_router(auth_router)
app.include_router(market_router)
app.include_router(orders_router)

@app.get("/")
def health_check():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {"version": APP_VERSION}
