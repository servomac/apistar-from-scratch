from apistar.test import TestClient
from project.views import welcome
from project.views import list_tasks, add_task

def test_welcome():
    """
    Testing a view directly.
    """
    data = welcome()
    assert data == {'message': 'Welcome to API Star!'}

client = TestClient()

def test_http_request():
    """
    Testing a view, using the test client.
    """
    response = client.get('http://localhost/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Welcome to API Star!'}

def test_list_tasks():
    assert list_tasks() == []

def test_add_task():
    new_task = {'definition': 'test task'}

    client = TestClient()
    response = client.post('/task/', new_task)
    assert response.status_code == 200

    result = new_task
    result['completed'] = False
    assert response.json() == result
 