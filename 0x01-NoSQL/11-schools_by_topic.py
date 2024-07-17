#!/usr/bin/env python3
""" list of schools in the mongodb collection """


import pymongo

def schools_by_topic(mongo_collection, topic):
    """ schools collection """
    list_items = mongo_collection.find({'topic': topic})
    return list_items
