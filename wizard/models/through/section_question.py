from django.db import models


class SectionQuestion(models.Model):
    position = models.PositiveIntegerField()
    question = models.ForeignKey('wizard.Question', on_delete=models.CASCADE)
    section = models.ForeignKey('wizard.Section', on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            ('position', 'question', 'section'),
        )

    def __str__(self):
        return '{} > {}'.format(self.section, self.question)