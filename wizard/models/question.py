from django.db import models


class Question(models.Model):
    field = models.ForeignKey('wizard.Field', on_delete=models.CASCADE)
    text = models.CharField(max_length=256)

    def __str__(self):
        return self.text