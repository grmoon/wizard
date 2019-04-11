from django.db import models
from django.contrib.postgres import fields as postgres_fields

from wizard.models.answers.answer import Answer

class FileAnswer(Answer):
    question = models.ForeignKey(
        'wizard.FileQuestion',
        on_delete=models.CASCADE,
        related_name='answers'
    )
