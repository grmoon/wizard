from rest_framework import viewsets

from wizard.models import Section
from wizard.serializers import SectionSerializer


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer