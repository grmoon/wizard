from rest_framework import viewsets

from wizard.models import Step
from wizard.serializers import StepSerializer


class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer