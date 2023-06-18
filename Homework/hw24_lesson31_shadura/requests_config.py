import json


object_url = 'https://api.restful-api.dev/objects'
object_headers = {'content-type': 'application/json'}

object_json_1 = json.dumps({
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
})

object_json_2 = json.dumps({
    "name": "Apple MacBook 17",
    "data": {
        "year": 2021,
        "price": 1599.99,
        "CPU model": "Intel Core i7",
        "Hard disk size": "1 TB",
        "color": "silver"
    }
})

list_json = [object_json_1, object_json_2]