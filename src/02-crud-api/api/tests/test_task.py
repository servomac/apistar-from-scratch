from apistar.test import TestClient

task_endpoint = '/task/'
client = TestClient()

def test_list_tasks():
    response = client.get(task_endpoint)
    assert response.status_code == 200
    assert response.json() == []

def test_add_task():
    new_task = {'definition': 'test task'}

    response = client.post(task_endpoint, new_task)
    assert response.status_code == 200

    result = new_task
    result['completed'] = False
    assert response.json() == result
