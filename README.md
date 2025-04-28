# Bhediya

## Setup
1. Copy `.env.example` → `.env` and fill in your credentials.
2. `pip install -r requirements.txt`
3. `uvicorn app.main:app --reload`

## Endpoints
- `GET /auth/login_url` → get user login URL  
- `POST /auth/session` → `{ "request_token": "..." }` → `{ "access_token": "..." }`  
- `GET /market/instruments`  
- `GET /market/quote?exchange=NSE&symbol=INFY`  
- `GET /orders/place` etc.

## Next Steps
- Persist user tokens in a DB  
- Add background tasks for WebSocket ticks  
- Wrap your signal/risk logic around these modules  
