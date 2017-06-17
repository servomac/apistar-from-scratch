from typing import List

from project.schemas import Task, TaskDefinition

tasks = []

def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}

def list_tasks() -> List[Task]:
    """
    Return a list of tasks
    """
    return [Task(t) for t in tasks]

def add_task(definition: TaskDefinition) -> Task:
    """
    Add a new task
    """
    new_task = Task({'definition': definition})
    tasks.append(new_task)
    return new_task
