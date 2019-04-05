from rest_framework import viewsets

from wizard.models import Trigger
from wizard.serializers import TriggerSerializer


class TriggerViewSet(viewsets.ModelViewSet):
    queryset = Trigger.objects.all()
    serializer_class = TriggerSerializer