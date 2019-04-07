from wizard.models import StepSection
from wizard.serializers import StepSectionSerializer
from wizard.views.mixins.filter_by_ids import FilterByIdsMixin


class StepSectionViewSet(FilterByIdsMixin):
    queryset = StepSection.objects.all()
    serializer_class = StepSectionSerializer