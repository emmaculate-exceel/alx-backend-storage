#!/usr/bin/env python3
""" list of schools in the mongodb collection """


import pymongo


def schools_by_topic(mongo_collection, topic):
    """ schools collection """
    topics_items =  mongo_collection.find({'topics': topic})
    return topics_items
