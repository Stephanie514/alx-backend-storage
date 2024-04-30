#!/usr/bin/env python3

"""
Inserts a new document in a collection based on kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: The PyMongo collection object.
        **kwargs: Keyword arguments representing the document fields and values.

    Returns:
        The new _id of the inserted document.
    """
    new_document_id = mongo_collection.insert_one(kwargs).inserted_id
    return new_document_id
