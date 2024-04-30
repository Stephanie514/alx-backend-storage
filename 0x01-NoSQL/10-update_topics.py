#!/usr/bin/env python3

"""
Changes all topics of a school document based on the name.
"""

def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    Args:
        mongo_collection: The PyMongo collection object.
        name (str): The school name to update.
        topics (list): The list of topics approached in the school.

    Returns:
        The number of documents updated.
    """
    result = mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})

    return result.modified_count
