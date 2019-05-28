# coding:utf-8
from my_dispatcher import api_add, api


@api_add
def hello(*args, **kwargs):

    return {"hello": "hello"}


@api_add
def test_flo(*args, **kwargs):
    from flosdk import flosdk
    info = flosdk.get_info()
    return {"info": info}


