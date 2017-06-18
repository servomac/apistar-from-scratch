from apistar.test import TestClient

"""
 TODO:
  - FIX the tests are interdependent
  - test the schema validation, it's not currently working
  - put: assert that have becomed permanently marked as True,
         and is not only the response
"""

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
    assert response.status_code == 201

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


def _task_id_endpoint(task_id):
    return f'{task_endpoint}{task_id}/'

def test_delete_task():
    response = client.delete(_task_id_endpoint(-1))
    assert response.status_code == 404

    existing_id = added_task.get('id')
    response = client.delete(_task_id_endpoint(existing_id))
    assert response.status_code == 204

    response = client.delete(_task_id_endpoint(existing_id))
    assert response.status_code == 404

def test_patch_task():
    response = client.patch(_task_id_endpoint(-1), {'completed': True})
    assert response.status_code == 404

    # new task, initially created as incomplete
    response = client.post(task_endpoint, new_task)
    assert response.status_code == 201
    new_task_serialized = response.json()
    assert new_task_serialized.get('completed') == False

    existing_id = new_task_serialized.get('id')
    response = client.patch(_task_id_endpoint(existing_id), {'completed': True})
    assert response.status_code == 200
    assert response.json() == dict(new_task_serialized, **{'completed': True})
