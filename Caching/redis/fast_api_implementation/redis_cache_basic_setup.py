import redis
from fastapi import FastAPI

app = FastAPI()

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # attempt to retrieve the item from Redis cache
    # If it exists, we return the cached data
    # If not, we simulate fetching the data and cache it using redis_client.set.
    cached_item = redis_client.get(f"item_{item_id}")
    
    if cached_item:
        return {"item_id": item_id, "cached": True, "data": cached_item.decode('utf-8')}
    
    # Simulate data fetching process
    item_data = f"Item data for {item_id}"
    
    # Store the item in Redis for future requests
    redis_client.set(f"item_{item_id}", item_data)
    
    return {"item_id": item_id, "cached": False, "data": item_data}