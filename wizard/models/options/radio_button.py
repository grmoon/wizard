from django.db import models

from wizard.models.options.option import Option


class RadioButtonOption(Option):
    field = models.ForeignKey(
        'wizard.RadioButtonField',
        related_name='options',
        on_delete=models.CASCADE
    )