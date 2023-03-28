from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Item(Model):
    id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()

    def __str__(self):
        return self.name


class User(Model):
    id = fields.IntField(pk=True, index=True)
    user_name = fields.CharField(max_length=255)
    first_name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)
    password = fields.CharField(max_length=255)

    def __str__(self):
        return self.user_name


item_pydantic = pydantic_model_creator(Item, name="Item", exclude=("id",))
item_pydanticOut = pydantic_model_creator(Item, name="ItemOut")
# for put, patch requests, exclude readonly fields, so that they should not change
item_pydanticUp = pydantic_model_creator(Item, name="ItemUp", exclude_readonly=True)


user_pydantic = pydantic_model_creator(User, name="User", exclude=("id",))
user_pydanticOut = pydantic_model_creator(User, name="UserOut", exclude=('password',))
# for put, patch requests, exclude readonly fields, so that they should not change
user_pydanticUp = pydantic_model_creator(User, name="UserUp", exclude_readonly=True)
