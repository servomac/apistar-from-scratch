from apistar.test import TestClient

task_endpoint = '/task/'
client = TestClient()

new_task = {'definition': 'test task'}
added_task = {'definition': 'test task', 'completed': False, 'id': 1}

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

    # add another task
    response = client.post(task_endpoint, new_task)

    # the same fields, but an autoincremented id
    # (maybe collection's ChainMap is more expressive?)
    second_added_task = dict(added_task, **{'id': 2})

    response = client.get(task_endpoint)
    assert response.status_code == 200
    assert response.json() == [added_task, second_added_task]
