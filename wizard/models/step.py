from django.db import models


class Step(models.Model):
    name = models.CharField(max_length=256, unique=True)
    sections = models.ManyToManyField('wizard.Section', through='wizard.StepSection')

    def __str__(self):
        return self.name