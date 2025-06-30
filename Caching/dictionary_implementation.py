import requests

cache = dict()

def get_article_from_server(url):
    """Fetches an article from the server"""
    
    print("Fetching article from server...")
    response = requests.get(url)
    return response.text

def get_article(url):
    """Gets an article, either from cache or by fetching it from the server"""

    print("Getting article...")
    if url not in cache:
        cache[url] = get_article_from_server(url)

    return cache[url]

get_article("https://realpython.com/sorting-algorithms-python/")
get_article("https://realpython.com/sorting-algorithms-python/")