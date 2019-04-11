from django.db import models

from wizard.models.questions.question import Question


class FileQuestion(Question):
    field = models.ForeignKey('wizard.FileField', on_delete=models.CASCADE)
