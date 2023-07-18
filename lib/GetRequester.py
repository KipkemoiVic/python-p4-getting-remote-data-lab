import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response =requests.get(self.url)
        return response.content

    def load_json(self):
        response_body = self.get_response_body()
        json_data = response_body.decode('utf-8')
        return json.loads(json_data)
# Added a load_json() method that decodes the response body and loads it into a Python dictionary using the json.loads() function.


# programs = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json").get_response_body()
# print(programs) 

json_data = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json").load_json()
print(json_data)