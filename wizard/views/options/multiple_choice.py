from rest_framework import viewsets

from wizard.models import MultipleChoiceOption
from wizard.serializers import MultipleChoiceOptionSerializer


class MultipleChoiceOptionViewSet(viewsets.ModelViewSet):
    queryset = MultipleChoiceOption.objects.all()
    serializer_class = MultipleChoiceOptionSerializer