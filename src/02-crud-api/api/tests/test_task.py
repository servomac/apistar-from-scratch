from apistar.test import TestClient

task_endpoint = '/task/'
client = TestClient()

new_task = {'definition': 'test task'}
added_task = {'definition': 'test task', 'completed': False}

def test_list_tasks():
    response = client.get(task_endpoint)
    assert response.status_code == 200
    assert response.json() == []

def test_add_task():
    response = client.post(task_endpoint, new_task)
    assert response.status_code == 200

    assert response.json() == added_task

def test_list_an_added_task():
    response = client.get(task_endpoint)
    assert response.status_code == 200
    assert response.json() == [added_task]

    test_add_task()
    response = client.get(task_endpoint)
    assert response.status_code == 200
    assert response.json() == [added_task, added_task]