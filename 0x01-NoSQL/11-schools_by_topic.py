#!/usr/bin/env python3
""" list of schools in the mongodb collection """


def schools_by_topic(mongo_collection, topic):
    """ schools collection """
    list_items = mongo_collection.find({'topic': topic}).topic()
    return list(list_items)
