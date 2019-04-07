from wizard.models import Trigger
from wizard.serializers import TriggerSerializer
from wizard.views.mixins.filter_by_ids import FilterByIdsMixin


class TriggerViewSet(FilterByIdsMixin):
    queryset = Trigger.objects.all()
    serializer_class = TriggerSerializer
