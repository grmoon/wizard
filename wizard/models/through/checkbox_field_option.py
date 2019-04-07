from django.db import models

from wizard.models.through.abstract_multiple_choice_field_option import AbstractMultipleChoiceFieldOption

class CheckboxFieldOption(AbstractMultipleChoiceFieldOption):
    exclusive = models.BooleanField(default=False)
    field = models.ForeignKey('wizard.CheckboxField', on_delete=models.CASCADE)
    required = models.BooleanField(default=False)

