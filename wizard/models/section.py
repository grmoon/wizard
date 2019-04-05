from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=256)
    position = models.PositiveIntegerField()
    step = models.ForeignKey(
        'wizard.Step',
        on_delete=models.CASCADE,
        related_name='sections'
    )

    class Meta:
        unique_together = (
            ('name', 'step'),
            ('position', 'step'),
        )

    def __str__(self):
        return '{}: {}'.format(self.step, self.name)