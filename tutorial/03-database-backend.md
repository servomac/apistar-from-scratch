# 03 - Database backend

*WORK IN PROGRESS*

Code for this chapter available [here](/src/03-database-backend).

In previous chapters we have presented apistar and constructed a rudimentary API to handle our own TODO list. But it lacks any kind of persistence!

In this section we will introduce the database backends of API Star and add a database to our project. We will be using [SQLAlchemy](https://www.sqlalchemy.org/), but the framework also offers suport for [Django ORM](https://github.com/tomchristie/apistar#django-orm).

## PostgreSQL

PostgreSQL will be used as our relational database. We need to install the postgres python connector, psycopg2, and SQLAlchemy to interact with the db, so update your `requirements.txt` and build again the docker-compose services.

```sh
psycopg2==2.7.1
SQLAlchemy==1.1.10
```

We will extend our `docker-compose.yml` with the definition of the new member of the stack, the db, that will be a dependency for the api container:

```
  api:
  [..]
    depends_on:
      - db

  db:
    image: postgres:9.6-alpine
    environment:
      POSTGRES_DB: "dbname"
      POSTGRES_USER: "user"
      POSTGRES_PASSWORD: "pass"
```

## Your first model

We will use [declarative base](http://docs.sqlalchemy.org/en/latest/orm/extensions/declarative/api.html) from SQLAlchemy to create our *Task* model. Create a new file `models.py`:

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()

class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    definition = Column(String(128))
    completed = Column(Boolean, default=False)

    def __repr__(self):
        return '<Task id={}>'.format(self.id)

```

## Settings and db integration

First of all, we need to say to our app where to find the db and the [metadata](http://docs.sqlalchemy.org/en/latest/orm/extensions/declarative/basic_use.html#accessing-the-metadata) from the SQLAlchemy declarative base.

Let's define the settings from environment variables. API Star has a class Environment that allows to easily read them. Create a new file `settings.py` in the project path:

```python
from apistar import environment, schema
from project.models import Base

class Env(environment.Environment):
    properties = {
        'DEBUG': schema.Boolean(default=False),
        'DATABASE_URL': schema.String(default='sqlite://'),
    }

env = Env()

settings = {
    'DEBUG': env['DEBUG'],
    'DATABASE': {
        'URL': env['DATABASE_URL'],
        'METADATA': Base.metadata,
    }
}
```
> Note that the settings `DATABASE` parameter is specific of SQLAlchemy. If you want to use Django ORM, take a look to the [APIStar readme](https://github.com/tomchristie/apistar#django-orm).

And pass those settings as an argument to your app constructor:

```python
# app.yml
[...]
from project.settings import settings

app = App(routes=routes, settings=settings)
```

Define the environment vars needed in the docker compose api service. Set debug as `True` and the database url to connect to the postgres db.

```
# docker-compose.yml
  api:
    [...]
    environment:
      - DATABASE_URL=postgresql+psycopg2://user:pass@db/dbname
      - DEBUG=True
```
> Note: Thanks to the internal docker dns I can directly write the name of the service on the database connection url! Take a look of the [SQLAlchemy](http://docs.sqlalchemy.org/en/latest/dialects/postgresql.html) PostgreSQL documentation to construct the URI.

### Commands: create_tables

Use `create_tables` command to create your tables. Import it from apistar and pass it to the App constructor.

```python
# app.py
from apistar.commands import create_tables
[...]

app = App(routes=routes, settings=settings, commands=[create_tables])
```

And invoke the command:

```
$ apistar create_tables
  Tables created
```

> Note: There is some work in progress for custom commands in the framework. See the issue [#65](https://github.com/tomchristie/apistar/issues/65) and pull request [#62](https://github.com/tomchristie/apistar/pull/62).

### Access the database from views

You can inject the [SQLAlchemy component](https://github.com/tomchristie/apistar/blob/38a5d7a307f268ca3e0e03f6a8779a643c545798/apistar/backends/sqlalchemy_backend.py) in the views. It has `engine`, `session_class` and `metadata` as attributes.

```
# views.py
from apistar.backends import SQLAlchemy
from project.models import Task as TaskModel

def add_task(db: SQLAlchemy, definition: TaskDefinition) -> Response:
    task = TaskModel(definition=definition)
    session = db.session_class()
    session.add(task)
    session.commit()
    return Response(Task(task), status=201)
```

## Testing

