from rest_framework import viewsets

from wizard.models import CheckboxFieldOption
from wizard.serializers import CheckboxFieldOptionSerializer


class CheckboxFieldOptionViewSet(viewsets.ModelViewSet):
    queryset = CheckboxFieldOption.objects.all()
    serializer_class = CheckboxFieldOptionSerializer