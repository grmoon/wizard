from django.contrib.postgres import fields as postgres_fields
from django.db import models

from wizard.models.generic import GenericModel


class Field(GenericModel):
    name = models.CharField(max_length=256)
    default = postgres_fields.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name
