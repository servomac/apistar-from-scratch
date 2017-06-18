from apistar import Include, Route
from apistar.docs import docs_routes
from apistar.statics import static_routes
from project.views import welcome
from project.views import list_tasks, add_task, delete_task, patch_task

task_routes = [
    Route('/', 'GET', list_tasks),
    Route('/', 'POST', add_task),
    Route('/{task_id}/', 'DELETE', delete_task),
    Route('/{task_id}/', 'PATCH', patch_task),
]

routes = [
    Route('/', 'GET', welcome),
    Include('/task', task_routes),
    Include('/docs', docs_routes),
    Include('/static', static_routes)
]
