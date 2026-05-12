import os
import logging
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
from contextlib import asynccontextmanager
import redis

logger = logging.getLogger("uvicorn.error")

def seed_redis(redis_client):
    try:
        if not redis_client.exists("STUDENT10"):
            redis_client.set("STUDENT10", 10)
            redis_client.set("BIGSALE", 30)
        logger.info("Redis seeded successfully")
    except redis.exceptions.ConnectionError:
        logger.warning("Could not seed Redis (connection failed). Will retry later.")

@asynccontextmanager
async def lifespan(app: FastAPI):
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
    r_client = redis.from_url(REDIS_URL, decode_responses=True)

    for attempt in range(5):
        try:
            r_client.ping()
            break
        except redis.exceptions.ConnectionError:
            logger.warning(f"Redis not ready, attempt {attempt+1}/5. Retrying...")
            import asyncio
            await asyncio.sleep(2)
    else:
        logger.error("Could not connect to Redis after multiple attempts")

    seed_redis(r_client)
    app.state.redis = r_client
    yield
    r_client.close()

app = FastAPI(title="Discount Service", lifespan=lifespan)

class DiscountRequest(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)
    price: float = Field(gt=0)
    promo_code: Optional[str] = None

class DiscountResponse(BaseModel):
    discount_percent: float
    discount_amount: float
    reason: str

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "discount-service"}

@app.post("/discounts/calculate", response_model=DiscountResponse)
async def calculate_discount(request: DiscountRequest):
    r = app.state.redis
    discount_percent = 0
    reason = "No discount applied"

    if request.promo_code:
        try:
            stored_discount = r.get(request.promo_code)
            if stored_discount:
                discount_percent = int(stored_discount)
                reason = f"Promo code '{request.promo_code}' applied"
        except redis.exceptions.ConnectionError:
            raise HTTPException(status_code=503, detail="Discount service temporarily unavailable")

    if discount_percent == 0 and request.quantity >= 10:
        discount_percent = 5
        reason = "Discount for (10+ items)"

    total_price = request.price * request.quantity
    discount_amount = total_price * (discount_percent / 100)

    return {
        "discount_percent": discount_percent,
        "discount_amount": discount_amount,
        "reason": reason,
    }