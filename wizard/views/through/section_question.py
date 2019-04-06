from rest_framework import viewsets

from wizard.models import SectionQuestion
from wizard.serializers import SectionQuestionSerializer


class SectionQuestionViewSet(viewsets.ModelViewSet):
    queryset = SectionQuestion.objects.all()
    serializer_class = SectionQuestionSerializer