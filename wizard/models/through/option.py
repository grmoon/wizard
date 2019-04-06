from django.db import models

from wizard.models import GenericModel

class OptionThroughModel(GenericModel):
    option = models.ForeignKey('wizard.Option', on_delete=models.CASCADE)
    position = models.PositiveIntegerField()

    class Meta:
        abstract = True
        unique_together = (
            ('position', 'field'),
            ('field', 'option'),
        )

    def __str__(self):
        return '{} > {}'.format(self.field, self.option)