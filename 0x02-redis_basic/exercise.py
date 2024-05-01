#!/usr/bin/env python3
"""
Module: cache.py
Description: Implements a Cache class using Redis.
"""

import redis
import uuid
from typing import Union


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis and returns the generated key.

        Args:
            data: Data to be stored. Can be a str, bytes, int, or float.

        Returns:
            str: The generated key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
