import requests

class RestClient:
    def __init__(self, host='http://127.0.0.1:5000/'):
        self.host = host
    
    def get_animals(self):
        response = requests.get(self.host + 'animals')
        animals = self.__parseResponse(response)
        return animals
    
    def get_people(self):
        response = requests.get(self.host + 'people')
        people = self.__parseResponse(response)
        return people

    def __parseResponse(self, response):
        list_to_return = []
        if response.status_code == 200:
            json = response.json()
            list_to_return = json['names']
        else:
            raise Exception("Expected OK status but got " + response.status_code)
        return list_to_return
