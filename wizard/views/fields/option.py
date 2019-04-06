from rest_framework import viewsets

from wizard.models import Option
from wizard.serializers import OptionSerializer


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer