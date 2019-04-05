from django.db import models


class Wizard(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.name