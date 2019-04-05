from rest_framework import viewsets

from wizard.models import RadioButtonField
from wizard.serializers import RadioButtonFieldSerializer


class RadioButtonFieldViewSet(viewsets.ModelViewSet):
    queryset = RadioButtonField.objects.all()
    serializer_class = RadioButtonFieldSerializer