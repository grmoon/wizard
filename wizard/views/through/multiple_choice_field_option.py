from rest_framework import viewsets

from wizard.models import MultipleChoiceFieldOption
from wizard.serializers import MultipleChoiceFieldOptionSerializer


class MultipleChoiceFieldOptionViewSet(viewsets.ModelViewSet):
    queryset = MultipleChoiceFieldOption.objects.all()
    serializer_class = MultipleChoiceFieldOptionSerializer