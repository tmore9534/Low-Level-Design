from abc import ABC, abstractmethod
import json
from typing import Dict, Any


# External service (Adaptee)
class WebService:
    def __init__(self, host: str):
        self.webHost = host

    def request(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        print(f"Sending request to {self.webHost} with data: {payload}")
        return {
            "text": "success",
            "status_code": 200
        }


# 1. Define a common interface (Target Interface)
class WebRequester(ABC):
    @abstractmethod
    def request(self, obj) -> Dict[str, Any]:
        pass


# 2. Implement the Adapter Class (Using `connect` method to attach WebService)
class WebAdapter(WebRequester):
    def __init__(self):
        self.webService = None  # Initially, no WebService is connected

    def connect(self, webService: WebService):
        self.webService = webService  # Assign the WebService instance
        print("Connected to:", self.webService.webHost)

    def request(self, obj) -> Dict[str, Any]:
        if not self.webService:
            raise ValueError("No WebService connected. Call connect() first.")
        
        json_data = self.get_json(obj)
        return self.webService.request(json_data)

    def get_json(self, obj) -> Dict[str, Any]:
        return json.dumps(obj.__dict__)  # Convert object attributes to JSON


# Object that needs to be converted
class Object:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


# WebClient interacts with the Adapter only
class WebClient:
    def __init__(self, webRequester: WebRequester):
        self.webRequester = webRequester

    def make_obj(self, id: int, name: str) -> Object:
        return Object(id, name)

    def do_work(self):
        obj = self.make_obj(1, "Test Object")
        response = self.webRequester.request(obj)
        print(f"Response: {response}")
        return response


# Main execution
webService = WebService("http://www.google.com")  # Creating WebService
webAdapter = WebAdapter()  # Create Adapter (without service initially)
webAdapter.connect(webService)  # Connect WebService using `connect()`
webClient = WebClient(webAdapter)  # Client only interacts with Adapter

webClient.do_work()
