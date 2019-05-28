# coding:utf-8
import requests
from my_dispatcher import api_add, api


@api_add
def get_difficulty(*args, **kwargs):
    """获取难度值"""
    r = requests.get("http://network.flo.cash/api/getdifficulty")

    if r.status_code != 200:
        return {"error": "get difficulty fail"}

    if r.json() != "":
        difficulty = str(r.json())

    return {
        "difficulty": difficulty or ""
    }


@api_add
def get_coin_supply(*args, **kwargs):
    """获取当前硬币总供给量"""
    r = requests.get("http://network.flo.cash/ext/getmoneysupply")
    if r.status_code != 200:
        return {"error": "get coin supply fail"}

    if r.json() != "":
        coin_supply = str(r.json())

    return {
        "coin_supply": coin_supply or ""
    }


@api_add
def get_network_hashps(*args, **kwargs):
    """全网算力"""
    r = requests.get("http://network.flo.cash/api/getnetworkhashps")
    if r.status_code != 200:
        return {"error": "get network hashps fail"}

    if r.json() != "":
        network_hashps = str(r.json()*pow(10, -9))[0:8] + " GH/s"

    return {
        "network_hashps": network_hashps or ""
    }


@api_add
def get_distribution(*args, **kwargs):
    """获取财富分配"""
    r = requests.get("http://network.flo.cash/ext/getdistribution")
    if r.status_code != 200:
        return {"error": "get coin supply fail"}

    if r.json() != "":
        distribution = str(r.json())

    return {
        "distribution": distribution or {}
    }


@api_add
def get_block_count(*args, **kwargs):
    """获取当前块数"""
    r = requests.get("http://network.flo.cash/api/getblockcount")
    if r.status_code != 200:
        return {"error": "get block count fail"}

    if r.json() != "":
        block_count = str(r.json())

    return {
        "block_count": block_count or ""
    }


@api_add
def get_node_count(*args, **kwargs):
    """获取节点数"""
    r = requests.get("http://network.flo.cash/api/getconnectioncount")
    if r.status_code != 200:
        return {"error": "get node count fail"}

    if r.json() != "":
        node_count = str(r.json())

    return {
        "node_count": node_count or ""
    }
