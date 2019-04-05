from django.db import models

from wizard.models.options.option import Option
from wizard.models.options.option_meta import OptionMeta


class RadioButtonOption(OptionMeta, Option):
    field = models.ForeignKey(
        'wizard.RadioButtonField',
        related_name='options',
        on_delete=models.CASCADE
    )