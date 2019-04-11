from django.db import models

from wizard.models.generic import GenericModel


class Question(GenericModel):
    text = models.CharField(max_length=256)

    def __str__(self):
        return self.text