from django.db import models

from wizard.models.fields.multiple_choice import MultipleChoiceField


class CheckboxField(MultipleChoiceField):
    options = models.ManyToManyField(
        'wizard.Option',
        through='wizard.CheckboxOption',
    )