from fastapi import FastAPI
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded


# Initialize the rate limiter with a function to get the client's IP address
limiter = Limiter(key_func=get_remote_address)
app = FastAPI()

# Attach the limiter to the app's state for global access
app.state.limiter = limiter

# Register the exception handler for rate limit exceeded errors
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# Define a GET endpoint at /home with a rate limit of 5 requests per minute
@app.get("/home")
@limiter.limit("5/minute")
async def homepage(request: Request):
    return PlainTextResponse("test")


# Define a GET endpoint at /mars with a rate limit of 5 requests per minute
@app.get("/mars")
@limiter.limit("5/minute")
async def homepage(request: Request, response: Response):
    return {"key": "value"}