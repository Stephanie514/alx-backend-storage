#!/usr/bin/env python3
"""
Module: cache.py
Description: Implements a Cache class using Redis.
"""

import redis
import uuid
from typing import Union, Callable
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = f"cache_calls:{method.__qualname__}"
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

class Cache:
    """
    Cache class for storing data in Redis.
    """

    def __init__(self):
        """
        Initializes a Cache object with a Redis client instance and
        flushes the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis and returns the generated key.

        Args:
            data: Data to be stored. Can be a str, bytes, int, or float.

        Returns:
            str: The generated key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        input_key = f"{self.store.__qualname__}:inputs"
        output_key = f"{self.store.__qualname__}:outputs"
        self._redis.rpush(input_key, str(data))
        self._redis.rpush(output_key, key)
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieves data from Redis using the given key and optionally applies a
        conversion function.

        Args:
            key (str): The key used to retrieve data from Redis.
            fn (Callable): Optional conversion function to be applied to
            the retrieved data.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data, optionally
            converted using the provided function.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieves data from Redis as a string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieves data from Redis as an integer.
        """
        return self.get(key, fn=int)
