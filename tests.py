import unittest
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


class TestAdditionEndpoint(unittest.TestCase):

    def test_for_valid_input(self):
        input_data = {
          "batchid": "id0101",
          "payload": [[1,2],[3,4]]
            }
        response = client.post("/addition/", json=input_data)
        assert response.status_code == 200
        assert response.json() == {'batchid': 'id0101', 'response': [3,4], 'status': 'Complete', 'started_at': 'started_time', 'completed_at' : 'completed_time'}


    def test_for_empty_input(self):
        input_data = {
            "batchid": "id0101",
            "payload": [[], []]
        }
        response = client.post("/addition/", json=input_data)
        assert response.status_code == 200
        assert response.json() == {'batchid': 'id0101', 'response': [0,0], 'status': 'Complete', 'started_at': 'started_time', 'completed_at' : 'completed_time'}

    def test_for_invalid_input(self):
        input_data = {
            "batchid": "id0101",
            "payload": [[1, 2], ['a', 4]]
        }
        response = client.post("/addition/", json=input_data)
        assert response.status_code == 500
        assert response.json() == {"detail": "Error occurred during adding number"}

if __name__ == "__main__":
    unittest.main()