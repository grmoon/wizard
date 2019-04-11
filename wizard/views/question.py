from wizard.models import JSONQuestion
from wizard.serializers import QuestionSerializer
from wizard.views.mixins.filter_by_ids import FilterByIdsMixin


class QuestionViewSet(FilterByIdsMixin):
    queryset = JSONQuestion.objects.all()
    serializer_class = QuestionSerializer
