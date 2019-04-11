from django.db import models

from wizard.models.base import BaseModel

class Wizard(BaseModel):
    name = models.CharField(max_length=256, unique=True)
    steps = models.ManyToManyField('wizard.Step', through='wizard.WizardStep')

    def __str__(self):
        return self.name