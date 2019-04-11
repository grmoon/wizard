from django.db import models

from wizard.models.base import BaseModel

class SectionQuestion(BaseModel):
    position = models.PositiveIntegerField()
    question = models.ForeignKey('wizard.Question', on_delete=models.CASCADE)
    section = models.ForeignKey('wizard.Section', on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            ('position', 'question', 'section'),
        )

    def __str__(self):
        return '{} > {}'.format(self.section, self.question)