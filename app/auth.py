from kiteconnect import KiteConnect
from fastapi import APIRouter, Request
from .config import API_KEY, API_SECRET, REDIRECT_URI

router = APIRouter(prefix="/auth", tags=["auth"])
kite = KiteConnect(api_key=API_KEY)

@router.get("/login_url")
def login_url():
    return {"login_url": kite.login_url(redirect_uri=REDIRECT_URI)}

@router.post("/session")
async def create_session(request: Request):
    data = await request.json()
    request_token = data.get("request_token")
    if not request_token:
        return {"error": "request_token required"}, 400

    session = kite.generate_session(request_token, api_secret=API_SECRET)
    access_token = session["access_token"]
    kite.set_access_token(access_token)
    # TODO: persist access_token for user
    return {"access_token": access_token}
