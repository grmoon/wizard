from wizard.models import Question
from wizard.serializers import QuestionSerializer
from wizard.views.mixins.filter_by_ids import FilterByIdsMixin


class QuestionViewSet(FilterByIdsMixin):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
