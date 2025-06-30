# LRU Caching in Python

## What Is LRU Caching?

**LRU (Least Recently Used) caching** stores recently used results and automatically removes the least recently accessed items when space is full. It helps speed up repeated operations like expensive function calls or API requests.

---

## Why Use It?

* Avoids redundant computation
* Boosts performance
* Saves system resources
* Built into Python via `functools.lru_cache`

---

## Basic Usage

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def compute(x):
    return x * x
```

* First call computes the result.
* Repeated calls with the same input return cached result.
* When `maxsize` is reached, the least recently used items are discarded.

---

## Extra Features

```python
compute.cache_info()
# Shows hits, misses, and cache size

compute.cache_clear()
# Manually clears the cache
```

---

## Limitations

* No built-in time-based expiration
* Only works with hashable arguments
* Cache is memory-only and reset on program restart

---

## Custom Time-Based LRU

To expire items after a duration:

```python
# @timed_lru_cache(seconds) — combines time and LRU eviction
# See previous implementation example
```

---

## Use Cases

* Memoizing function results
* API or database response caching
* Repeated computations in ML/data processing