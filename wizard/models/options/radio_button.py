from django.db import models

from wizard.models.options.abstract_multiple_choice import AbstractMultipleChoiceOption

class RadioButtonOption(AbstractMultipleChoiceOption):
    field = models.ForeignKey('wizard.RadioButtonField', on_delete=models.CASCADE)

