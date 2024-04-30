#!/usr/bin/env python3

"""
Script that provides stats about Nginx logs stored in MongoDB.

Database: logs
Collection: nginx

Displays:
1. Total number of logs.
2. Number of logs for each HTTP method (GET, POST, PUT, PATCH, DELETE).
3. Number of logs with method=GET and path=/status.

Usage:
    python nginx_logs_stats.py
"""

from pymongo import MongoClient

def nginx_logs_stats():
    """
    Provides stats about Nginx logs stored in MongoDB.
    """
    client = MongoClient('mongodb://localhost:27017/')

    db = client.logs
    collection = db.nginx

    all_logs = collection.count_documents({})

    print(f"{total_logs} logs where {total_logs} is the number of documents in this collection")

    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in http_methods}

    print("\nMethods:")
    for method, count in method_counts.items():
        print(f"\t{count} {method}")

    stat_count = collection.count_documents({"method": "GET", "path": "/status"})

    print(f"\t{stat_count} method=GET path=/status")
