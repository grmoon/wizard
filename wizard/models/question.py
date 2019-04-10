from django.contrib.postgres import fields as postgres_fields
from django.db import models


class Question(models.Model):
    default = postgres_fields.JSONField(blank=True, null=True)
    field = models.ForeignKey('wizard.Field', on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    triggers = models.ManyToManyField(
        'self',
        through='wizard.Trigger',
        symmetrical=False
    )

    def __str__(self):
        return self.text