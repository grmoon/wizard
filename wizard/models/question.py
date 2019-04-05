from django.db import models


class Question(models.Model):
    field = models.ForeignKey('wizard.Field', on_delete=models.CASCADE)
    position = models.PositiveIntegerField()
    section = models.ForeignKey(
        'wizard.Section',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    text = models.CharField(max_length=256)

    class Meta:
        unique_together = (
            ('section', 'position'),
        )

    def __str__(self):
        return '{}: {}'.format(self.section, self.text)