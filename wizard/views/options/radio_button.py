from rest_framework import viewsets

from wizard.models import RadioButtonOption
from wizard.serializers import RadioButtonOptionSerializer


class RadioButtonOptionViewSet(viewsets.ModelViewSet):
    queryset = RadioButtonOption.objects.all()
    serializer_class = RadioButtonOptionSerializer