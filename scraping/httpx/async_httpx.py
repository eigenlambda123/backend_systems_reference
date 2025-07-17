import asyncio
import httpx

# Define a reusable async function to fetch a URL
async def fetch_url(client: httpx.AsyncClient, url: str) -> dict:
    """
    Fetch a URL using an async HTTP client and return the response details.
    """
    try:
        response = await client.get(url)
        return {
            "url": url,
            "status": response.status_code,
            "length": len(response.text),
            "ok": response.is_success
        }
    except httpx.RequestError as e:
        return {
            "url": url,
            "error": str(e)
        }

# Main async function
async def main():
    # List of URLs to fetch
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://python.org",
        "https://httpbin.org/status/404",  # Force a 404 for testing
        "https://invalid.url.test"         # Invalid URL to show error handling
    ]

    # Reuse one client for all requests
    async with httpx.AsyncClient(timeout=10.0) as client:
        tasks = [fetch_url(client, url) for url in urls]
        results = await asyncio.gather(*tasks)

    # Display results
    for result in results:
        if "error" in result:
            print(f"[ERROR] {result['url']} → {result['error']}")
        else:
            print(f"[OK] {result['url']} → Status: {result['status']} | Length: {result['length']}")

if __name__ == "__main__":
    asyncio.run(main())