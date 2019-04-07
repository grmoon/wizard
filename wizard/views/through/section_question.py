from wizard.models import SectionQuestion
from wizard.serializers import SectionQuestionSerializer
from wizard.views.mixins.filter_by_ids import FilterByIdsMixin


class SectionQuestionViewSet(FilterByIdsMixin):
    queryset = SectionQuestion.objects.all()
    serializer_class = SectionQuestionSerializer
