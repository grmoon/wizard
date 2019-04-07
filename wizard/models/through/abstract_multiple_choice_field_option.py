from django.db import models

from wizard.models.through.multiple_choice_field_option import MultipleChoiceFieldOption


class AbstractMultipleChoiceFieldOption(MultipleChoiceFieldOption):
    option = models.ForeignKey('wizard.Option', on_delete=models.CASCADE)
    position = models.PositiveIntegerField()

    class Meta:
        abstract = True
        unique_together = (
            ('position', 'field', 'option'),
        )

    def __str__(self):
        return '{} > {}'.format(self.field, self.option)