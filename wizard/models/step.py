from django.db import models

from wizard.models.base import BaseModel


class Step(BaseModel):
    name = models.CharField(max_length=256, unique=True)
    sections = models.ManyToManyField('wizard.Section', through='wizard.StepSection')

    def __str__(self):
        return self.name