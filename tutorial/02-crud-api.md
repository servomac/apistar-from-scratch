# 02 - A basic CRUD API with TDD

Code for this chapter available [here](/src/02-crud-api/).

With our fresh environment we will start to get hands on with API Star. In this section we will construct a simple CRUD (*Create, Read, Update and Delete*) api **to manage a TODO list**.

We will put special enfasis on testing, using `py.test` testing framework, which is included in API Star. We will follow some principles of TDD (*Test Driven Development*).

## A TODO List

The TODO List is the 'hello world' of the XXI century. In this basic example, a user could create or delete a **Task**, as well as mark it as completed. It should also list every **Task**, and maybe allow to filter by a completed query string param.

The endpoints of our API will be:

 * `GET /task/`: Retrieve a list of tasks.
 * `POST /task/`: Create a new task.
 * `GET /task/{id}/`: Retrieve an specific task by id.
 * `PUT /task/{id}/`: Update some field of an specific task (i.e. mark as completed)
 * `DELETE /task/{id}/`: Delete a task by id. 

## Routes and views

TODO codi y TDD

## Type your views using Schemas

API Star provides a typing system to define your API interface. `Schemas` are defined as specification of input/output data contracts for your views, validating your input and serializing your output (as libraries such as [marshmallow](https://marshmallow.readthedocs.io/en/latest/) do).

