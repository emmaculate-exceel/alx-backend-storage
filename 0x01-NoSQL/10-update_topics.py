#!/usr/bin/env python3
""" updating mongodb collection """


def update_topics(mongo_collection, name, topics):
    """ updating collection """
    mongo_collection.update_many({'name': name}, {$set: {'topics': 'topics'}})
