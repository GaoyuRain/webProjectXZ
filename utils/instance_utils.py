"""
author :admin
Date : 2021/07/08
Description : 实例化注解
"""
from functools import wraps
from threading import RLock


def singleton(cls):
    """装饰类的装饰器-线程安全"""
    instances = {}
    locker = RLock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with locker:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        # print(instances.__str__())
        return instances[cls]

    return wrapper
