import json

from rest_framework import authentication
from rest_framework.response import Response
from rest_framework.views import APIView

from wizard.models import JSONAnswer, FileAnswer, Upload
from wizard.serializers import AnswerSerializer, UploadSerializer


class AnswerBulkAPIView(APIView):
    authentication_classes = (authentication.SessionAuthentication,)

    def post(self, request):
        json_answers = self._create_or_update_json_answers(request)
        (file_answers, uploads) = self._create_or_update_file_answers(request)

        answers = list(json_answers) + list(file_answers)

        data = {
            'answers': AnswerSerializer(answers, many=True).data,
            'uploads': UploadSerializer(uploads, many=True).data,
        }

        return Response(data)

    def _create_or_update_json_answers(self, request):
        json_answers = json.loads(request.data['json_answers'])

        (
            answer_data_to_create,
            answer_data_to_update,
        ) = self._partition_answer_data(json_answers)

        updated_answer_ids = self._update_json_answers(answer_data_to_update)
        created_answer_ids = self._create_json_answers(answer_data_to_create)

        answer_ids = updated_answer_ids + created_answer_ids

        return JSONAnswer.objects.filter(pk__in=answer_ids)

    def _create_or_update_file_answers(self, request):
        file_answers = json.loads(request.data['file_answers'])

        (
            answer_data_to_create,
            answer_data_to_update,
        ) = self._partition_answer_data(file_answers)

        (updated_answer_ids, updated_uploads) = self._update_file_answers(answer_data_to_update, request)
        (created_answer_ids, created_uploads) = self._create_file_answers(answer_data_to_create, request)

        answer_ids = updated_answer_ids + created_answer_ids
        uploads = created_uploads + updated_uploads

        return (FileAnswer.objects.filter(pk__in=answer_ids), uploads)

    def _partition_answer_data(self, answer_data):
        answer_data_to_update = []
        answer_data_to_create = []

        for answer_datum in answer_data:
            if 'id' in answer_datum:
                answer_data_to_update.append(answer_datum)
            else:
                answer_data_to_create.append(answer_datum)

        return (answer_data_to_create, answer_data_to_update,)

    def _create_json_answers(self, answer_data_to_create):
        answers = []

        for answer_datum in answer_data_to_create:
            answer = JSONAnswer(**answer_datum)
            answers.append(answer)

        JSONAnswer.objects.bulk_create(answers)

        answer_ids = [answer_id for answer_id in map(lambda answer: answer.id, answers)]

        return answer_ids

    def _update_json_answers(self, answer_data_to_update):
        answer_ids = []

        for answer_datum in answer_data_to_update:
            answer_id = answer_datum['id']
            answer_ids.append(answer_id)
            JSONAnswer.objects.filter(pk=answer_id).update(**answer_datum)

        return answer_ids

    def _create_file_answers(self, answer_data_to_create, request):
        answers = []
        file_indices_by_question_id = {}

        for answer_datum in answer_data_to_create:
            file_indices = answer_datum.pop('file_indices')

            question_id = answer_datum['question_id']
            file_indices_by_question_id[question_id] = file_indices

            answer = FileAnswer(**answer_datum)
            answers.append(answer)

        FileAnswer.objects.bulk_create(answers)

        answer_ids = []
        uploads = []
        all_files = request.FILES.getlist('files')

        for answer in answers:
            answer_ids.append(answer.id)
            file_indices = file_indices_by_question_id[answer.question_id]

            for index in file_indices:
                _file = all_files[index]
                uploads.append(Upload(answer=answer, file=_file))

        Upload.objects.bulk_create(uploads)

        return (answer_ids, uploads)

    def _update_file_answers(self, answer_data_to_update, request):
        answer_ids = []
        all_files = request.FILES.getlist('files')
        uploads_to_create = []
        uploads_to_delete = []

        for answer_datum in answer_data_to_update:
            file_indices = answer_datum.pop('file_indices')

            answer_id = answer_datum['id']
            answer_ids.append(answer_id)

            FileAnswer.objects\
                .prefetch_related('value')\
                .filter(pk=answer_id)\
                .update(**answer_datum)

            if len(file_indices) > 0:
                answer = FileAnswer.objects.get(pk=answer_id)
                uploads_to_delete += list(answer.value.values_list('pk', flat=True))

                for index in file_indices:
                    _file = all_files[index]
                    uploads_to_create.append(Upload(answer=answer, file=_file))

        Upload.objects.bulk_create(uploads_to_create)
        # Upload.objects.filter(pk__in=uploads_to_delete).delete()

        return (answer_ids, uploads_to_create)

    @staticmethod
    def _create_uploads(request, indices):
        for index in indices:
            _file = request.data.getlist('files')[index]


