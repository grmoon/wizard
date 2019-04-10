from django.db import models

from wizard.models.options.multiple_choice import MultipleChoiceOption

class SelectOption(MultipleChoiceOption):
    disabled = models.BooleanField(default=False)
    field = models.ForeignKey('wizard.SelectField', on_delete=models.CASCADE)

