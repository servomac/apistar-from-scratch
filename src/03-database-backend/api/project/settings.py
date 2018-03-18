from apistar import environment, schema
from project.models import Base

class Env(environment.Environment):
    properties = {
        'DEBUG': schema.Boolean(default=False),
        'DATABASE_URL': schema.String(default='sqlite:///test.db'),
    }

env = Env()

settings = {
    'DEBUG': env['DEBUG'],
    'DATABASE': {
        'URL': env['DATABASE_URL'],
        'METADATA': Base.metadata,
    }
}
