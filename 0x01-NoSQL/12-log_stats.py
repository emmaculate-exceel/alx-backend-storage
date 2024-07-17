#!/usr/bin/env python3
""" nginx logs """


from pymongo import MongoClient


if __name__ == '__main__':
    client_con = MongoClient()
    nginx_col = client_con.logs.nginx.count_documents({})
    print(f"{nginx_col} logs")
    print("Methods:")

    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = nginx_col.count_documents({'method': method})
        print(f'{\tmethod {method}: {count}')

    nb_counts = nginx_col.count_documents({'method': 'GET', 'path': '/status'})
    print(f'{nb_counts} status check')
