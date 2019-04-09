from django.db import models

from wizard.models.fields.multiple_choice import MultipleChoiceField


class RadioButtonField(MultipleChoiceField):
    required = models.BooleanField(default=False)
    options = models.ManyToManyField(
        'wizard.Option',
        through='wizard.RadioButtonOption',
    )