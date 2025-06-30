# Caching in Software Systems

## What Is Caching?

Caching stores frequently accessed data in a faster storage (usually memory) to improve performance, reduce load, and avoid redundant operations like network calls or expensive computations.

---

## Why Cache?

* **Speed**: Faster access to data
* **Efficiency**: Reduces CPU, network, and database usage
* **Scalability**: Handles more users with fewer resources
* **Responsiveness**: Improves user experience

---

## Common Strategies

| Strategy      | Description                              |
| ------------- | ---------------------------------------- |
| Cache-Aside   | App reads/writes to cache manually       |
| Write-Through | Cache and database update together       |
| Read-Through  | Cache fetches missing data automatically |
| TTL           | Cache expires after a fixed time         |
| LRU           | Least Recently Used items are evicted    |

---

## Cache Types

* **In-Memory**: Fastest (e.g., `lru_cache`, Redis)
* **Disk-Based**: For large data like ML models
* **Distributed**: Shared cache across servers (e.g., Redis, Memcached)
* **Browser**: Static assets cached on the client side

---

## Example: Python `lru_cache`

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def compute(x):
    return x * x
```

---

## When Not to Cache

* The data changes frequently
* Serving stale data is a risk
* Strong consistency is required

---

## Summary

| Use Case       | Tool                      |
| -------------- | ------------------------- |
| Function calls | `lru_cache`               |
| API responses  | `httpx + cache`           |
| ML predictions | `joblib`, Redis           |
| Web pages      | CDN or HTTP cache headers |

Caching is a powerful performance tool—when used with awareness of trade-offs like staleness and invalidation complexity.