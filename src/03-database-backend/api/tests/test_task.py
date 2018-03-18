import pytest

import apistar
from apistar.backends import SQLAlchemy
from apistar.test import TestClient
from apistar.test import CommandLineRunner

from app import app


runner = CommandLineRunner(app)


@pytest.fixture
def clear_db(scope="function"):
    yield
    db_backend = SQLAlchemy.build(app.settings)
    db_backend.drop_tables()


def test_list_tasks(monkeypatch, clear_db):
    client = TestClient(app)

    def mock_get_current_app():
        return app

    monkeypatch.setattr(apistar.main, 'get_current_app', mock_get_current_app)

    result = runner.invoke(['create_tables'])
    assert 'Tables created' in result.output

    response = client.get('/task/')
    assert response.status_code == 200
    assert response.json() == []


def test_add_task(monkeypatch, clear_db):
    client = TestClient(app)

    def mock_get_current_app():
        return app

    monkeypatch.setattr(apistar.main, 'get_current_app', mock_get_current_app)

    runner.invoke(['create_tables'])
    response = client.post('/task/', {'definition': 'test task'})
    assert response.status_code == 201

    assert response.json() == {
        'definition': 'test task',
        'completed': False,
        'id': 1,
    }

# TODO pending https://github.com/tomchristie/apistar/issues/6
#def test_add_task_without_data():
#    response = client.post(task_endpoint)
#    assert response.status_code == 422
#    assert response.json() == {'error': 'You should provide a definition of the task.'}


# def test_list_an_added_task(client):
#     response = client.get(task_endpoint)
#     assert response.status_code == 200
#     assert response.json() == [added_task]

#     # add another task
#     response = client.post(task_endpoint, new_task)

#     # the same fields, but an autoincremented id
#     # (maybe collection's ChainMap is more expressive?)
#     second_added_task = dict(added_task, **{'id': 2})

#     response = client.get(task_endpoint)
#     assert response.status_code == 200
#     assert response.json() == [added_task, second_added_task]


# def _task_id_endpoint(task_id):
#     return f'{task_endpoint}{task_id}/'

# def test_delete_task(client):
#     response = client.delete(_task_id_endpoint(-1))
#     assert response.status_code == 404

#     existing_id = added_task.get('id')
#     response = client.delete(_task_id_endpoint(existing_id))
#     assert response.status_code == 204

#     response = client.delete(_task_id_endpoint(existing_id))
#     assert response.status_code == 404

# def test_patch_task(client):
#     response = client.patch(_task_id_endpoint(-1), {'completed': True})
#     assert response.status_code == 404

#     # new task, initially created as incomplete
#     response = client.post(task_endpoint, new_task)
#     assert response.status_code == 201
#     new_task_serialized = response.json()
#     assert new_task_serialized.get('completed') == False

#     existing_id = new_task_serialized.get('id')
#     response = client.patch(_task_id_endpoint(existing_id), {'completed': True})
#     assert response.status_code == 200
#     assert response.json() == dict(new_task_serialized, **{'completed': True})
