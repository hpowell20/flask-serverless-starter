from core.model import BaseModel
from pynamodb.attributes import UnicodeAttribute, BooleanAttribute


class TodoModel(BaseModel):
    class Meta:
        simple_ame = 'todos'
        region = BaseModel.Meta.default_region

    id = UnicodeAttribute(hash_key=True)
    title = UnicodeAttribute()
    description = UnicodeAttribute(null=True)
    is_complete = BooleanAttribute(default=False)
