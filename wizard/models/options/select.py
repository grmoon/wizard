from django.db import models

from wizard.models.options.abstract_multiple_choice import AbstractMultipleChoiceOption

class SelectOption(AbstractMultipleChoiceOption):
    disabled = models.BooleanField(default=False)
    field = models.ForeignKey('wizard.SelectField', on_delete=models.CASCADE)

