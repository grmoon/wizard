from django.db import models

from wizard.models.fields.field import Field


class InputField(Field):
    required = models.BooleanField(default=False)

    class Meta:
        abstract = True