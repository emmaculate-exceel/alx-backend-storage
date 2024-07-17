#!/usr/bin/env python3
""" nginx logs """

import pymongo
from pymongo import MongoClient


if __name__ == '__main__':
    client_con = MongoClient('mongodb://127.0.0.1:27017')
    nginx_col = client_con.logs.nginx
    nginx_count = nginx_col.count_documents({})
    print(f'{nginx_count} logs')

    print('Methods:')

    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = nginx_col.count_documents({'method': method})
        print(f'\tmethod {method}: {count}')

    nb_counts = nginx_col.count_documents({'method': 'GET', 'path': '/status'})
    print(f'{nb_counts} status check')
