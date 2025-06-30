import feedparser
import requests
import ssl
import time
from functools import lru_cache, wraps
from datetime import datetime, timedelta

if hasattr(ssl, "_create_unverified_context"):
    """This is a workaround for SSL verification issues"""

    ssl._create_default_https_context = ssl._create_unverified_context


def timed_lru_cache(seconds: int, maxsize: int = 128):
    """
    Decorator to cache function results with a time-to-live (TTL) expiration
    """

    def wrapper_cache(func):
        """
        Wraps the function with an LRU cache that expires after a specified time
        """

        func = lru_cache(maxsize=maxsize)(func) # Apply LRU caching
        func.lifetime = timedelta(seconds=seconds) # Set the lifetime of the cache
        func.expiration = datetime.utcnow() + func.lifetime # Set the initial expiration time

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            """Checks if the cache has expired and clears it if necessary"""
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime

            return func(*args, **kwargs) # Call the cached function
        return wrapped_func # Return the wrapped function
    return wrapper_cache # Return the decorator



@timed_lru_cache(10) # Cache for 10 seconds
def get_article_from_server(url):
    """Fetches an article from the server"""
    
    print("Fetching article from server...")
    response = requests.get(url)
    return response.text


def monitor(url):
    """Monitors a feed for articles containing the word 'python' in the title"""
    maxlen = 45
    while True:
        print("\nChecking feed...")
        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:
            if "python" in entry.title.lower():
                truncated_title = (
                    entry.title[:maxlen] + "..."
                    if len(entry.title) > maxlen
                    else entry.title
                )
                print(
                    "Match found:",
                    truncated_title,
                    len(get_article_from_server(entry.link)),
                )

        time.sleep(5)


monitor("https://realpython.com/atom.xml")