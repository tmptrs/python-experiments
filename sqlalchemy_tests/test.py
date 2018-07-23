from random import randint

def generator():
    while(1):
        yield randint(1,5)

def decorator(func):
    def newfunc(*args, **kwargs):
        print('this function has been decorated')
        return func(*args, **kwargs)
    return newfunc

import sqlalchemy.dialects.postgresql.json

from sqlalchemy.dialects.postgresql import BIGINT
