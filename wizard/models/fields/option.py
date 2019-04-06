from django.db import models


class Option(models.Model):
    label = models.CharField(max_length=256)
    value = models.CharField(max_length=256)

    def __str__(self):
        return self.label