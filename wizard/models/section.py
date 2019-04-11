from django.db import models

from wizard.models.base import BaseModel


class Section(BaseModel):
    name = models.CharField(max_length=256)
    questions = models.ManyToManyField('wizard.Question', through='wizard.SectionQuestion')

    def __str__(self):
        return self.name