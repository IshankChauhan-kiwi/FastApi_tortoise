"""
Models file
"""
from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Job(Model):
    id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()

    def __str__(self):
        return self.name


job_pydantic = pydantic_model_creator(Job, name="Job", exclude=("id",))
job_pydanticOut = pydantic_model_creator(Job, name="JobOut")
# for put, patch requests, exclude readonly fields, so that they should not change
job_pydanticUp = pydantic_model_creator(Job, name="JobUp", exclude_readonly=True)



