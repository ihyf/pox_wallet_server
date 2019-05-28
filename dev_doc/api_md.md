# flo-获取难度值
---
URL:http://149.28.56.184:9000/api
## 上行

```json
{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "get_difficulty",
	"params": {

	}
}
```

## 下行
```json
{
    "result": {
        "difficulty": "2662.65787070532" //难度值
    },
    "id": 1,
    "jsonrpc": "2.0"
}
```


# flo-获取当前flo总量
---
URL:http://149.28.56.184:9000/api
## 上行

```json
{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "get_coin_supply",
	"params": {

	}
}
```

## 下行
```json
{
    "result": {
        "coin_supply": "151073657.95824438"  //总量
    },
    "id": 1,
    "jsonrpc": "2.0"
}
```

# flo-获取当前区块高度
---
URL:http://149.28.56.184:9000/api
## 上行

```json
{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "get_block_count",
	"params": {

	}
}
```

## 下行
```json
{
    "result": {
        "block_count": "3450820"
    },
    "id": 1,
    "jsonrpc": "2.0"
}
```

# flo-获取当前节点数量
---
URL:http://149.28.56.184:9000/api
## 上行

```json
{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "get_node_count",
	"params": {

	}
}
```

## 下行
```json
{
    "result": {
        "node_count": "100"
    },
    "id": 1,
    "jsonrpc": "2.0"
}}
```
# flo-获取全网算力
---
URL:http://149.28.56.184:9000/api
## 上行

```json
{
	"jsonrpc": "2.0",
	"id": 1,
	"method": "get_network_hashps",
	"params": {

	}
}
```

## 下行
```json
{
    "result": {
        "network_hashps": "265.7371 GH/s"
    },
    "id": 1,
    "jsonrpc": "2.0"
}
```
