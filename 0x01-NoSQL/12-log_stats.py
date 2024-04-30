#!/usr/bin/env python3

"""
A python script that provides some stats
about Nginx logs stored in MongoDB:

Database: logs
Collection: nginx

Displays:
1. Total number of logs.
2. Number of logs for each HTTP method (GET, POST, PUT, PATCH, DELETE).
3. Number of logs with method=GET and path=/status.
"""

from pymongo import MongoClient


def nginx_logs_stats():
    """
    A function that connects to MongoDB, retrieves
    log stats, and prints the total number of
    logs, counts methods such as
    GET, POST, PUT, PATCH, and DELETE, and checks the status.
    """
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    total_logs = coll.count_documents({})
    print(f"{total_logs} logs where {total_logs} is no of docs in collection")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = coll.count_documents({"method": method})
        print(f"\t{count} {method}")

    cnt_stat_check = coll.count_documents({"method": "GET", "path": "/status"})
    print(f"{cnt_stat_check} method=GET\npath=/status")


if __name__ == "__main__":
    nginx_logs_stats()
