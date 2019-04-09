from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import authentication

from wizard.models import Answer
from wizard.serializers import AnswerSerializer


class AnswerBulkAPIView(APIView):
    authentication_classes = (authentication.SessionAuthentication,)

    def post(self, request):
        (
            answer_datum_to_create,
            answer_datum_to_update,
        ) = self._partition_answer_data(request.data)

        updated_answer_ids = self._update_answers(answer_datum_to_update)
        created_answer_ids = self._create_answers(answer_datum_to_create)
        answer_ids = updated_answer_ids + created_answer_ids
        answers = Answer.objects.filter(pk__in=answer_ids)

        data = AnswerSerializer(answers, many=True).data

        return Response(data)

    def _partition_answer_data(self, answer_data):
        answer_datum_to_update = []
        answer_datum_to_create = []

        for answer_datum in answer_data:
            if 'id' in answer_datum:
                answer_datum_to_update.append(answer_datum)
            else:
                answer_datum_to_create.append(answer_datum)

        return (answer_datum_to_create, answer_datum_to_update,)

    def _create_answers(self, answer_datum_to_create):
        answers = []

        for answer_datum in answer_datum_to_create:
            answer = Answer(**answer_datum)
            answers.append(answer)

        Answer.objects.bulk_create(answers)

        answer_ids = [answer_id for answer_id in map(lambda answer: answer.id, answers)]

        return answer_ids

    def _update_answers(self, answer_datum_to_update):
        answer_ids = []

        for answer_datum in answer_datum_to_update:
            answer_id = answer_datum['id']
            answer_ids.append(answer_id)
            Answer.objects.filter(pk=answer_id).update(**answer_datum)

        return answer_ids

    # queryset = Answer.objects.all()
    # serializer_class = AnswerSerializer

    # def _get_by_question_ids(self, question_ids):
    #     answers = self.queryset.filter(question__in=question_ids, user=self.request.user)
    #     context = { 'request': self.request }
    #     data = self.serializer_class(answers, context=context, many=True).data

    #     return Response(data)

    # def list(self, *args, **kwargs):
    #     question_ids = list(map(lambda x: int(x), self.request.query_params.getlist('question_ids[]')))

    #     if len(question_ids) > 0:
    #         response = self._get_by_question_ids(question_ids)
    #     else:
    #         response = super().list(*args, **kwargs)

    #     return response
