#!/usr/bin/env python3

"""
Python function that returns all students sorted by average score.

Prototype: def top_students(mongo_collection):
mongo_collection will be the pymongo collection object
The top must be ordered
The average score must be part of each item returned with key = averageScore
"""

def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    """
    return mongo_collection.find(
        {},
        {"_id": 1, "name": 1, "averageScore": 1}
    ).sort("averageScore", -1)
