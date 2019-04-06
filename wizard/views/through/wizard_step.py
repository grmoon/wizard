from rest_framework import viewsets

from wizard.models import WizardStep
from wizard.serializers import WizardStepSerializer


class WizardStepViewSet(viewsets.ModelViewSet):
    queryset = WizardStep.objects.all()
    serializer_class = WizardStepSerializer