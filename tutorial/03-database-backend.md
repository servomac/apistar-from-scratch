# 03 - Database backend

*WORK IN PROGRESS*

Code for this chapter available [here](/src/03-database-backend).

In previous chapters we have presented apistar and constructed a rudimentary API to handle our own TODO list. But it lacks any kind of persistence!

In this section we will introduce the database backends of API Star and add a database to our project. We will be using [SQLAlchemy](https://www.sqlalchemy.org/), but the framework also offers suport for [Django ORM](https://github.com/tomchristie/apistar#django-orm).

## PostgreSQL

PostgreSQL will be used as our relational database. We need to install the postgres python connector, psycopg2, and SQLAlchemy to interact with the db, so update your requirements.txt and build again the docker-compose services.

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
    image: postgresql:9.6-alpine
    environment:
      POSTGRES_DB: "db"
      POSTGRES_USER: "user"
      POSTGRES_PASSWORD: "pass"
```

## Settings and db integration

First of all, ¡we need to say to our app where to find the db! Let's define the settings from environment variables: API Star has a class Environment that allows to easily read them.

Create a new file `settings.py` in the project path:

```python
from apistar import environment, schema

class Env(environment.Environment):
    properties = {
        'DEBUG': schema.Boolean(default=False),
        'DATABASE_URL': schema.String(default='sqlite://')
    }

env = Env()

settings = {
    'DATABASE': {
        'URL': env['DATABASE_URL']
    }
}
```

And pass those as an argument to your app constructor:

```python
# app.yml
[...]
from project.settings import settings

app = App(routes=routes, settings=settings)
```

In our api service definition in the `docker-compose.yml` we will add the environment vars needed. I will set debug as True and the database url to be able to connect to the postgres db.

```
  api:
    [...]
    environment:
      [...]
      - DATABASE_URL='postgresql://db/postgres'
      - DEBUG=True
```
> Note: Thanks to the internal docker dns I can directly write the name of the service on the database connection url!

## Your first model



### Commands: create_tables

## Testing with mocks

