from rest_framework import viewsets

from wizard.models import CheckboxOption
from wizard.serializers import CheckboxOptionSerializer


class CheckboxOptionViewSet(viewsets.ModelViewSet):
    queryset = CheckboxOption.objects.all()
    serializer_class = CheckboxOptionSerializer