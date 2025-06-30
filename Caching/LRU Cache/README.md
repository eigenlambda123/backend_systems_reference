# LRU Caching Strategy in Python

## Overview

**LRU (Least Recently Used) caching** is a memory optimization technique used to store the most recently accessed items, automatically discarding the least recently used ones when the cache exceeds its size limit. This helps improve performance in programs that repeatedly access expensive-to-compute or fetch data.

Python’s built-in `functools.lru_cache` decorator provides a simple and powerful way to implement this strategy.

---

## Why Use LRU Cache?

* **Improves performance** by storing the results of expensive function calls.
* **Avoids recomputation** for identical calls with the same arguments.
* **Manages memory efficiently** by limiting cache size.
* **Transparent and easy to use** via Python decorators.

---

## How It Works

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_function(x):
    print(f"Computing for {x}")
    return x * x
```

* The first call: computes and stores the result.
* Later calls with the same argument: returns result from cache.
* Once 128 unique calls are made, **oldest unused entries are evicted**.

---

## Parameters

### `@lru_cache(maxsize=128, typed=False)`

| Parameter | Description                                                                                  |
| --------- | -------------------------------------------------------------------------------------------- |
| `maxsize` | Maximum number of recent calls to cache. If set to `None`, the cache can grow without bound. |
| `typed`   | If `True`, calls with different types are cached separately (e.g., `3` vs `3.0`).            |

---

## Cache Methods

When using `lru_cache`, the decorated function gains useful attributes:

```python
expensive_function.cache_info()
# returns: CacheInfo(hits=3, misses=2, maxsize=128, currsize=2)

expensive_function.cache_clear()
# clears the cache
```

---

## Extending With Time-Based Expiration

The default `lru_cache` **does not expire entries based on time**. To handle dynamic content (e.g., articles, APIs), combine it with a **timed expiration strategy**:

### Custom `@timed_lru_cache` Decorator:

```python
from functools import lru_cache, wraps
from datetime import datetime, timedelta

def timed_lru_cache(seconds: int, maxsize: int = 128):
    def wrapper(func):
        func = lru_cache(maxsize=maxsize)(func)
        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped(*args, **kwargs):
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime
            return func(*args, **kwargs)

        return wrapped
    return wrapper
```

This approach allows cached entries to **refresh automatically** after a given duration.

---

## Use Cases

* Web Scraping or Feed Monitoring (e.g., Atom/RSS articles)
* API Response Caching
* Database Query Memoization
* Function Result Caching in Machine Learning pipelines

---

## Example

```python
@timed_lru_cache(60)
def fetch_article(url):
    print("Fetching from network...")
    return requests.get(url).text
```

Within 60 seconds, repeated calls to `fetch_article(url)` will return cached results. After that, the data is refetched.


---

## ✅ Summary

| Feature           | `lru_cache` | `timed_lru_cache` (custom) |
| ----------------- | ----------- | -------------------------- |
| Memoization       | ✅           | ✅                          |
| Size-limited      | ✅           | ✅                          |
| Time-based expiry | ❌           | ✅                          |
| Built-in support  | ✅           | ❌ (custom wrapper)         |

---

## Installation

No installation needed. `lru_cache` is part of Python’s standard library from **Python 3.2+**.

---

## References

* Python Docs: [`functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache)
* Real Python: [Caching in Python With lru\_cache](https://realpython.com/lru-cache-python/)
* PEP 476: HTTPS verification update info (related to feedparser usage)
