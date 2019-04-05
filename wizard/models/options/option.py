from django.db import models

from wizard.models.generic import GenericModel


class Option(models.Model):
    label = models.CharField(max_length=256)
    position = models.PositiveIntegerField()
    value = models.CharField(max_length=256)

    class Meta:
        abstract = True
        unique_together = (
            ('field', 'label'),
            ('field', 'position'),
            ('field', 'value'),
        )

    def __str__(self):
        return self.label
