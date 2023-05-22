import requests
import json


class ApiToJsonFile:
    def api_response_to_json_file(self, http_request, json_file):
        response = requests.get(http_request, headers={"Content-Type": "application/json"})
        data = response.json()
        with open('ex.json', 'w') as file:
            json.dump(data, file, indent=4)

api_processing_1 = ApiToJsonFile()
api_processing_1.api_response_to_json_file('http://numbersapi.com/random/year', 'ex.json')