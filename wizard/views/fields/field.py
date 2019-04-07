from wizard.models import Field
from wizard.serializers import FieldSerializer
from wizard.views.mixins.filter_by_ids import FilterByIdsMixin


class FieldViewSet(FilterByIdsMixin):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer