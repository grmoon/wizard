from django.db import models


class StepSection(models.Model):
    position = models.PositiveIntegerField()
    section = models.ForeignKey('wizard.Section', on_delete=models.CASCADE)
    step = models.ForeignKey('wizard.Step', on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            ('position', 'step', 'section'),
        )

    def __str__(self):
        return '{} > {}'.format(self.step, self.section)