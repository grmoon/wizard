from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=256)
    questions = models.ManyToManyField('wizard.Question', through='wizard.SectionQuestion')

    def __str__(self):
        return self.name