from django.db import models

from wizard.models.through.abstract_multiple_choice_field_option import AbstractMultipleChoiceFieldOption

class RadioButtonFieldOption(AbstractMultipleChoiceFieldOption):
    field = models.ForeignKey('wizard.RadioButtonField', on_delete=models.CASCADE)

