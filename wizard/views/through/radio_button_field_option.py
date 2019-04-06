from rest_framework import viewsets

from wizard.models import RadioButtonFieldOption
from wizard.serializers import RadioButtonFieldOptionSerializer


class RadioButtonFieldOptionViewSet(viewsets.ModelViewSet):
    queryset = RadioButtonFieldOption.objects.all()
    serializer_class = RadioButtonFieldOptionSerializer