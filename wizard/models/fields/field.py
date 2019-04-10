from django.db import models

from wizard.models.generic import GenericModel


class Field(GenericModel):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name
