from django.db import models

from wizard.models.fields.multiple_choice import MultipleChoiceField


class SelectField(MultipleChoiceField):
    autocomplete = models.BooleanField(default=False)
    autofocus = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)
    multiple = models.BooleanField(default=False)
    options = models.ManyToManyField(
        'wizard.Option',
        through='wizard.SelectOption',
    )
    required = models.BooleanField(default=False)
    size = models.IntegerField(blank=True, null=True)