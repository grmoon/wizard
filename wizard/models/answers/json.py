from django.db import models
from django.contrib.postgres import fields as postgres_fields

from wizard.models.answers.answer import Answer


class JSONAnswer(Answer):
    question = models.ForeignKey(
        'wizard.JSONQuestion',
        on_delete=models.CASCADE,
        related_name='answers'
    )
    value = postgres_fields.JSONField()

    class Meta:
        unique_together = (('question', 'user'),)
