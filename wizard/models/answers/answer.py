from django.db import models

from wizard.models.base import BaseModel

class Answer(BaseModel):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        abstract = True
        unique_together = (('question', 'user'),)

    def __str__(self):
        return "{}'s response to {}: {}".format(self.user.username, self.question.text, self.value)