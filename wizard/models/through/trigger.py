from django.contrib.postgres import fields
from django.core.exceptions import ValidationError
from django.db import models

from wizard.models.base import BaseModel

class Trigger(BaseModel):
    CONDITION_E = 'E'
    CONDITION_GT = 'GT'
    CONDITION_GTE = 'GTE'
    CONDITION_IN = 'IN'
    CONDITION_LT = 'LT'
    CONDITION_LTE = 'LTE'

    CONDITIONS = (
        (CONDITION_E, 'Value == Answer'),
        (CONDITION_GT, 'Value > Answer'),
        (CONDITION_GTE, 'Value >= Answer'),
        (CONDITION_LT, 'Value < Answer'),
        (CONDITION_LTE, 'Value <= Answer'),
        (CONDITION_IN, 'Value in Answer'),
    )

    from_question = models.ForeignKey(
        'wizard.JSONQuestion',
        on_delete=models.CASCADE
    )
    position = models.PositiveIntegerField()
    condition = models.CharField(max_length=256, choices=CONDITIONS, default=CONDITION_E)
    to_question = models.ForeignKey(
        'wizard.JSONQuestion',
        on_delete=models.CASCADE,
        related_name='triggered_by'
    )
    value = fields.JSONField()

    class Meta:
        unique_together = (
            ('position', 'from_question', 'to_question'),
            ('to_question', 'from_question', 'value', 'condition'),
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