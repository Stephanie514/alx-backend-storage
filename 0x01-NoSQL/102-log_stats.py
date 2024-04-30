#!/usr/bin/env python3

"""
Improved script to provide stats about Nginx logs stored in MongoDB.

Usage:
    python log_stats.py <database_name> <collection_name>
"""

import sys
from pymongo import MongoClient


def get_log_stats(database_name, collection_name):
    """
    Retrieves log stats from MongoDB and prints them.

    Args:
        database_name: Name of the MongoDB database.
        collection_name: Name of the MongoDB collection.

    Returns:
        None
    """
    try:
        # Connect to MongoDB
        client = MongoClient()
        db = client[database_name]
        collection = db[collection_name]

        # Total number of documents
        total_logs = collection.count_documents({})
        print(f"{total_logs} logs")

        # Count methods
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        print("Methods:")
        for method in methods:
            count = collection.count_documents({"method": method})
            print(f"    method {method}: {count}")

        # Count status check
        count_status_check = collection.count_documents({"method": "GET", "path": "/status"})
        print(f"{count_status_check} status check")

        # Top 10 IPs
        print("Top 10 IPs:")
        pipeline = [
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10}
        ]
        top_ips = collection.aggregate(pipeline)
        for index, ip in enumerate(top_ips, start=1):
            print(f"    {ip['_id']}: {ip['count']}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python log_stats.py <database_name> <collection_name>")
        sys.exit(1)

    database_name = sys.argv[1]
    collection_name = sys.argv[2]
    get_log_stats(database_name, collection_name)
