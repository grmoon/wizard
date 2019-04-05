from rest_framework import viewsets

from wizard.models import Wizard
from wizard.serializers import WizardSerializer


class WizardViewSet(viewsets.ModelViewSet):
    queryset = Wizard.objects.all()
    serializer_class = WizardSerializer