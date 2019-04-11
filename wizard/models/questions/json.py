from django.contrib.postgres import fields as postgres_fields
from django.db import models
from wizard.models.questions.question import Question


class JSONQuestion(Question):
    default = postgres_fields.JSONField(blank=True, null=True)
    field = models.ForeignKey('wizard.JSONField', on_delete=models.CASCADE)
    triggers = models.ManyToManyField(
        'self',
        through='wizard.Trigger',
        symmetrical=False
    )
