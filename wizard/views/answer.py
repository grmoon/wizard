from rest_framework import viewsets

from wizard.models import Answer
from wizard.serializers import AnswerSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer