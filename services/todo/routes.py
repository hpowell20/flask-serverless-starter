import uuid

from core import errors
from datetime import datetime
from flask import Blueprint, jsonify
from webargs.flaskparser import use_kwargs
from .model import TodoModel
from .resource import todo_schema

import logging
logger = logging.getLogger(__name__)
blueprint = Blueprint('todo', __name__)


@blueprint.route('/todos', methods=["GET"])
def list_todo_items():
    todo_items = TodoModel.scan()

    response = []

    for item in todo_items:
        response.append(todo_schema.dump(item).data)

    return jsonify(response)


@blueprint.route('/todos', methods=["POST"])
@use_kwargs(todo_schema, locations=('json',))
def add_todo_item(**kwargs):
    todo_item = TodoModel(id=str(uuid.uuid4()),
                          title=kwargs['title'],
                          description=kwargs['description'])

    todo_item.save()

    response = jsonify(todo_schema.dump(todo_item).data)
    response.status_code = 201
    return response


@blueprint.route('/todos/<todo_id>', methods=["GET"])
def retrieve_organization(todo_id):
    todo = retrieve_todo(todo_id)
    return jsonify(todo_schema.dump(todo).data)


@blueprint.route('/todos/<todo_id>', methods=["PUT"])
@use_kwargs(todo_schema, locations=('json',))
def update_organization(todo_id, **kwargs):
    todo_item = retrieve_todo(todo_id)

    todo_item.update(
        actions=[
            TodoModel.title.set(kwargs['title']),
            TodoModel.description.set(kwargs['description']),
            TodoModel.updated.set(datetime.now())
        ]
    )

    response = jsonify(todo_schema.dump(todo_item).data)
    response.status_code = 201
    return response


def retrieve_todo(todo_id):
    '''

    :param todo_id:
    :return:
    '''
    try:
        return TodoModel.get(hash_key=todo_id)
    except TodoModel.DoesNotExist:
        message = 'Todo ID {} does not exist'.format(todo_id)
        raise errors.ResourceValidationError(messages={'name': [message]})