from django.db import models
from django.contrib.postgres import fields as postgres_fields


class Answer(models.Model):
    question = models.ForeignKey(
        'wizard.Question',
        on_delete=models.CASCADE,
        related_name='answers'
    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    value = postgres_fields.JSONField()

    class Meta:
        unique_together = (('question', 'user'),)

    def __str__(self):
        return str(self.value)