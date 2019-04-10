from django.db import models

from wizard.models.options.multiple_choice import MultipleChoiceOption

class RadioButtonOption(MultipleChoiceOption):
    field = models.ForeignKey('wizard.RadioButtonField', on_delete=models.CASCADE)

