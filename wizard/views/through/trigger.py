from rest_framework import viewsets
from rest_framework.response import Response

from wizard.models import Trigger
from wizard.serializers import TriggerSerializer


class TriggerViewSet(viewsets.ModelViewSet):
    queryset = Trigger.objects.all()
    serializer_class = TriggerSerializer

    def _get_by_from_question_ids(self, from_question_ids):
        triggers = self.queryset.filter(from_question_id__in=from_question_ids)
        context = { 'request': self.request }
        data = self.serializer_class(triggers, context=context, many=True).data

        return Response(data)

    def list(self, *args, **kwargs):
        from_question_ids = list(map(lambda x: int(x), self.request.query_params.getlist('from_question_ids[]')))

        if len(from_question_ids) > 0:
            response = self._get_by_from_question_ids(from_question_ids)
        else:
            response = super().list(*args, **kwargs)

        return response
