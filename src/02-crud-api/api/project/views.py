import itertools
from typing import List

from apistar.http import Response
from apistar.schema import Boolean

from project.schemas import Task, TaskDefinition

# global variable representing the
# list of tasks, indexed by id
tasks = {}

# https://stackoverflow.com/questions/9604516/simple-number-generator
counter = itertools.count(1).__next__

def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}

def list_tasks() -> List[Task]:
    return [Task(tasks[id]) for id in tasks]

def add_task(definition: TaskDefinition) -> Response:
    """
    Add a new task. It receives its definition as an argument
    and sets an autoincremental id in the Task constructor.

    Returns the created serialized object and 201 status code on success.

    TODO:
     - maybe this counter could be implemented as an injectable component?
    """
    id = counter()
    tasks[id] = {
        'id': id,
        'definition': definition,
        'completed': False,
    }
    return Response(Task(tasks[id]), status=201)

def delete_task(task_id: int) -> Response:
    if task_id not in tasks:
        return Response({}, status=404)

    del tasks[task_id]
    return Response({}, status=204)

def patch_task(task_id: int, completed: Boolean) -> Response:
    """
    Mark an specific task referenced by id as completed/incompleted.

    Returns the entire updated serialized object and 200 status code on success.
    """
    if task_id not in tasks:
        return Response({}, status=404)

    tasks[task_id]['completed'] = completed
    return Response(Task(tasks[task_id]), status=200)
