from django.db import models

from wizard.models.base import BaseModel


class Upload(BaseModel):
    answer = models.ForeignKey(
        'wizard.FileAnswer',
        on_delete=models.CASCADE,
        related_name='value'
    )
    file = models.FileField(blank=True, null=True)
