from rest_framework import viewsets
from rest_framework.response import Response

from wizard.models import Question
from wizard.serializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    # def retrieve(self, *args, **kwargs):
    #     import pdb
    #     pdb.set_trace()
    #     question = Question.objects.first()
    #     context = { 'request': self.request }
    #     data = QuestionSerializer(question, context=context).data
    #     data.pop('triggers')

    #     return Response(data)