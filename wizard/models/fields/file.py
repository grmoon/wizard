from django.db import models

from wizard.models.fields.field import Field

class FileField(Field):
    accept = models.CharField(max_length=256, blank=True, null=True)
    multiple = models.BooleanField(default=False)
    required = models.BooleanField(default=False)
