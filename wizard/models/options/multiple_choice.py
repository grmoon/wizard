from django.db import models

from wizard.models.base import BaseModel

class MultipleChoiceOption(BaseModel):
    option = models.ForeignKey('wizard.Option', on_delete=models.CASCADE)
    position = models.PositiveIntegerField()

    class Meta:
        abstract = True
        unique_together = (
            ('position', 'field', 'option'),
        )

    def __str__(self):
        return '{} > {}'.format(self.field, self.option)