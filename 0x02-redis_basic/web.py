#!/usr/bin/env python3
"""
Module: web.py
Description: Implements a function to retrieve HTML content from
a URL and cache the result.
"""

import requests
import redis
from typing import Optional

def get_page(url: str) -> Optional[str]:
    """
    Retrieve the HTML content of a URL and cache the result with
    an expiration time of 10 seconds.

    Args:
        url (str): The URL to retrieve the HTML content from.

    Returns:
        str: The HTML content of the URL.
    """
    try:
        redis_client = redis.Redis()

        cached_html = redis_client.get(url)
        if cached_html:
            return cached_html.decode()

        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text

        redis_client.setex(url, 10, html_content)

        count_key = f"count:{url}"
        redis_client.incr(count_key)

        return html_content
    except requests.RequestException:
        return None
