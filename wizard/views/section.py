from wizard.models import Section
from wizard.serializers import SectionSerializer
from wizard.views.mixins.filter_by_ids import FilterByIdsMixin


class SectionViewSet(FilterByIdsMixin):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer