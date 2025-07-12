import redis
from fastapi import FastAPI

app = FastAPI()

redis_client = redis.Redis(host='localhost', port=6379, db=0)

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    cached_item = redis_client.get(f"item_{item_id}")
    
    if cached_item:
        return {"item_id": item_id, "cached": True, "data": cached_item.decode('utf-8')}
    
    item_data = f"Item data for {item_id}"
    
    # Store the item in Redis with an expiration time of 1 hour (3600 seconds)
    redis_client.setex(f"item_{item_id}", 3600, item_data)
    
    return {"item_id": item_id, "cached": False, "data": item_data}