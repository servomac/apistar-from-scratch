from apistar import App
from apistar.commands import create_tables

from project.routes import routes
from project.settings import settings

app = App(routes=routes, settings=settings, commands=[create_tables])
