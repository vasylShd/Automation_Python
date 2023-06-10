import requests
import json

object_url = 'https://api.restful-api.dev/objects'

object_headers = {
    'content-type':'application/json'
}
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
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2020,
            "price": 1849.99,
            "CPU model": "Intel Core i7",
            "Hard disk size": "1 TB",
            "display size": "17`"
        }
    })

object = requests.post(object_url, data=object_json_1, headers=object_headers)
object_id = object.json().get('id')

def test_post():
    object_1 = requests.post(object_url, data=object_json_1, headers=object_headers)
    assert object_1.status_code == 200

def test_get():
    get_request = requests.get(object_url + '/' + object_id, headers=object_headers)
    assert get_request.json().get('data') == {'CPU model': 'Intel Core i9', 'Hard disk size': '1 TB', 'price': 1849.99, 'year': 2019}

def test_put():
    put_request = requests.put(object_url + '/' + object_id, data=object_json_2, headers=object_headers)
    assert put_request.json().get('data') == {'CPU model': 'Intel Core i7', 'Hard disk size': '1 TB', 'display size': '17`', 'price': 1849.99, 'year': 2020}

def test_patch():
    patch_json = json.dumps({"name": "DELL Latitude 3420"})
    patch_request = requests.patch(object_url + '/' + object_id, data=patch_json, headers=object_headers)
    assert patch_request.json().get('name') == 'DELL Latitude 3420'

def test_object_delete():
    del_request = requests.delete(object_url + '/' + object_id)
    assert del_request.json().get('message') == f'Object with id = {object_id} has been deleted.'
    check_request = requests.get(object_url + '/' + object_id, headers=object_headers)
    assert check_request.status_code == 404