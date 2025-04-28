import threading
from kiteconnect import KiteTicker
from .config import API_KEY
from .auth import kite

kws = KiteTicker(API_KEY, None)  # set access token per user/session

def on_connect(ws, response):
    # subscribe example token list
    ws.subscribe([408065])
    ws.set_mode(ws.MODE_FULL, [408065])

def on_ticks(ws, ticks):
    print("Received ticks:", ticks)
    # TODO: dispatch to your strategy engine

def start_ws(access_token, tokens: list):
    kw = KiteTicker(API_KEY, access_token)
    kw.on_connect = on_connect
    kw.on_ticks   = on_ticks
    # run in background thread
    thread = threading.Thread(target=kw.connect, kwargs={"threaded": True})
    thread.start()
    return thread
