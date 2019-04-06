from django.contrib.postgres import fields
from django.core.exceptions import ValidationError
from django.db import models


class Trigger(models.Model):
    from_question = models.ForeignKey(
        'wizard.Question',
        on_delete=models.CASCADE
    )
    position = models.PositiveIntegerField()
    to_question = models.ForeignKey(
        'wizard.Question',
        on_delete=models.CASCADE,
        related_name='triggered_by'
    )
    value = fields.JSONField()

    class Meta:
        unique_together = (
            ('position', 'from_question'),
            ('to_question', 'from_question'),
        )

        constraints = [
            models.CheckConstraint(
                check=~models.Q(from_question=models.F('to_question')),
                name='trigger__different_questions'
            ),
        ]

    def clean(self, *args, **kwargs):
        if self.from_question_id == self.to_question_id:
            error_message = 'to_question and from_question must be different.'

            raise ValidationError({
                'to_question': error_message,
                'from_question': error_message,
            })

        super().clean(*args, **kwargs)


    def __str__(self):
        return '{} > {}'.format(self.from_question, self.to_question)