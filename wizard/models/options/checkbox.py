from django.db import models

from wizard.models.options.multiple_choice import MultipleChoiceOption

class CheckboxOption(MultipleChoiceOption):
    exclusive = models.BooleanField(default=False)
    field = models.ForeignKey('wizard.CheckboxField', on_delete=models.CASCADE)
    required = models.BooleanField(default=False)

