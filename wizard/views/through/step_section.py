from rest_framework import viewsets

from wizard.models import StepSection
from wizard.serializers import StepSectionSerializer


class StepSectionViewSet(viewsets.ModelViewSet):
    queryset = StepSection.objects.all()
    serializer_class = StepSectionSerializer