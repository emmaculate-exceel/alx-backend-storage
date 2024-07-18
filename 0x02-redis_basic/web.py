#!/usr/bin/env python3
""" an expiring web cache / tracker """


import requests
import redis
import time
from functools import wraps

# Initialize Redis connection
redis_client = redis.Redis()

def get_page(url: str) -> str:
    """ checking the url """
    # Check if the URL has been accessed before
    count_key = f"count:{url}"
    cached_html = redis_client.get(url)

    if cached_html:
        # If cached content exists, return it
        print(f"Cache hit for {url}")
        return cached_html.decode('utf-8')

    # Otherwise, fetch the HTML content from the URL
    print(f"Fetching {url} from the web")
    response = requests.get(url)
    html_content = response.text

    # Cache the fetched HTML with a 10-second expiration time
    redis_client.setex(url, 10, html_content)

    # Track the number of accesses for this URL
    current_count = redis_client.incr(count_key)
    print(f"Access count for {url}: {current_count}")

    return html_content

# Example usage:
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/1000/url/https://example.com"
    print(get_page(url))
    time.sleep(5)  # Simulate some time passing
    print(get_page(url))
