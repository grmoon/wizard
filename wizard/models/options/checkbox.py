from django.db import models

from wizard.models.options.abstract_multiple_choice import AbstractMultipleChoiceOption

class CheckboxOption(AbstractMultipleChoiceOption):
    exclusive = models.BooleanField(default=False)
    field = models.ForeignKey('wizard.CheckboxField', on_delete=models.CASCADE)
    required = models.BooleanField(default=False)

