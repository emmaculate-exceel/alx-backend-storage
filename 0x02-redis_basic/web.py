#!/usr/bin/env python3
'''
module with tools for request caching and tracking.
'''
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
'''
module-level Redis instance.
'''


def data_cacher(method: Callable) -> Callable:
    '''
    Cache output for data.
    '''
    @wraps(method)
    def invoker(url) -> str:
        '''
        wrapper function output.
        '''
        redis_store.incr(f'count:{url}')
        output = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        output = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    '''
    Returning the content of a URL after caching the request's and response,
    and tracking the request.
    '''
    return requests.get(url).text
