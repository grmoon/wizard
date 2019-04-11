from django.db import models

from wizard.models.base import BaseModel

class Option(BaseModel):
    label = models.CharField(max_length=256)
    value = models.CharField(max_length=256)

    def __str__(self):
        return self.label