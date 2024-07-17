#!/usr/bin/env python3
""" listing all documents in a collection in mongodb """


def list_all(mongo_collection):
    """ function to list all collection """
    return mongo_collection.find()
