from django.db import models

from wizard.models.through.option import OptionThroughModel

class RadioButtonFieldOption(OptionThroughModel):
    field = models.ForeignKey('wizard.RadioButtonField', on_delete=models.CASCADE)