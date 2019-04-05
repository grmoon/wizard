from django.db import models


class Step(models.Model):
    position = models.PositiveIntegerField()
    wizard = models.ForeignKey(
        'wizard.Wizard',
        on_delete=models.CASCADE,
        related_name='steps'
    )

    class Meta:
        unique_together = (
            ('position', 'wizard'),
        )

    def __str__(self):
        return 'Step {}'.format(self.position)