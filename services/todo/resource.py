from core.resource import ma
from marshmallow import fields


class TodoSchema(ma.Schema):
    class Meta:
        strict = True

    id = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(missing="")
    is_complete = fields.Bool(dump_only=True)


todo_schema = TodoSchema()
