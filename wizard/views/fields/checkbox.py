from rest_framework import viewsets

from wizard.models import CheckboxField
from wizard.serializers import CheckboxFieldSerializer


class CheckboxFieldViewSet(viewsets.ModelViewSet):
    queryset = CheckboxField.objects.all()
    serializer_class = CheckboxFieldSerializer