# API

```python
client_controller = client.client
```

## Class Name

`APIController`

## Methods

* [Get a List of Items](../../doc/controllers/api.md#get-a-list-of-items)
* [Create a New Item](../../doc/controllers/api.md#create-a-new-item)


# Get a List of Items

```python
def get_a_list_of_items(self)
```

## Response Type

[`ItemsResponse`](../../doc/models/items-response.md)

## Example Usage

```python
result = client_controller.get_a_list_of_items()
```


# Create a New Item

```python
def create_a_new_item(self,
                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ItemsRequest`](../../doc/models/items-request.md) | Body, Required | - |

## Response Type

`void`

## Example Usage

```python
body = ItemsRequest()

client_controller.create_a_new_item(body)
```

