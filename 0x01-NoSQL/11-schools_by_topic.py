#!/usr/bin/env python3

"""
Returns the list of schools having a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: The PyMongo collection object.
        topic (str): The topic searched.

    Returns:
        A list of school documents that have the specified topic.
    """
    schools = mongo_collection.find({"topics": topic})

    return list(schools)
