from rest_framework import viewsets
from rest_framework.response import Response

from wizard.models import Answer
from wizard.serializers import AnswerSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def _get_by_question_ids(self, question_ids):
        answers = self.queryset.filter(question__in=question_ids, user=self.request.user)
        context = { 'request': self.request }
        data = self.serializer_class(answers, context=context, many=True).data

        return Response(data)

    def list(self, *args, **kwargs):
        question_ids = list(map(lambda x: int(x), self.request.query_params.getlist('question_ids[]')))

        if len(question_ids) > 0:
            response = self._get_by_question_ids(question_ids)
        else:
            response = super().list(*args, **kwargs)

        return response
