from django.db import models


class Step(models.Model):
    position = models.PositiveIntegerField()

    def __str__(self):
        return 'Step {}'.format(self.position)