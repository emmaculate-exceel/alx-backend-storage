#!/usr/bin/env python3
""" inserting to the mongodb collection """


def insert_school(mongo_collection, **kwargs):
    """ inserting using keywords arguments """
    return mongo_collection.insert_one(kwargs).inserted_id
