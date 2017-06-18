# 03 - Database backend

Code for this chapter available [here](/src/03-database-backend).

In previous chapters we have presented apistar and constructed a rudimentary API to handle our own TODO list. But it lacks any kind of persistence!

In this section we will introduce the database backends of API Star and add a database to our project. We will be using [SQLAlchemy](https://www.sqlalchemy.org/), but the framework also offers suport for [Django ORM](https://github.com/tomchristie/apistar#django-orm).

## Settings

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

## Your first model

### Commands: create_tables

## Testing with mocks

