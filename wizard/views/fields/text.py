from rest_framework import viewsets

from wizard.models import TextField
from wizard.serializers import TextFieldSerializer


class TextFieldViewSet(viewsets.ModelViewSet):
    queryset = TextField.objects.all()
    serializer_class = TextFieldSerializer