from django.db import models


class Trigger(models.Model):
    option = models.ForeignKey(
        'wizard.Option',
        on_delete=models.CASCADE,
        related_name='triggers'
    )
    question = models.ForeignKey(
        'wizard.Question',
        on_delete=models.CASCADE,
        related_name='triggered_by'
    )
    position = models.PositiveIntegerField()

    class Meta:
        unique_together = (
            ('option', 'position'),
        )

    def __str__(self):
        return '{} -> {}'.format(self.option, self.question)