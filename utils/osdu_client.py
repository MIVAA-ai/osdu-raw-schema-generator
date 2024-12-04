import requests
class OSDUClient:
    def __init__(self, config):
        self.base_url = config['base_url']
        self.headers = config['headers']

    def create_schema_in_osdu(self, payload):
        query_url = f"{self.base_url}/api/schema-service/v1/schema"  # API endpoint for creating schema
        response = requests.post(query_url, headers=self.headers, json=payload)  # API request
        data = response.json()  # Parse response as JSON
        return data
