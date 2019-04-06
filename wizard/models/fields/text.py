from django.db import models

from wizard.models.fields.field import Field

class TextField(Field):
    maxlength = models.IntegerField(blank=True, null=True)
    minlength = models.IntegerField(blank=True, null=True)
    pattern = models.CharField(max_length=256, blank=True, null=True)
    placeholder = models.CharField(max_length=256, blank=True, null=True)
    readonly = models.BooleanField(default=False)
    required = models.BooleanField(default=False)
    size = models.IntegerField(blank=True, null=True)
    spellcheck = models.BooleanField(default=False)
