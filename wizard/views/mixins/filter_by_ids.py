
from rest_framework import viewsets
from rest_framework.response import Response


class FilterByIdsMixin(viewsets.ModelViewSet):
    def _get_by_ids(self, ids):
        records = self.queryset.filter(pk__in=ids)
        context = { 'request': self.request }
        data = self.serializer_class(records, context=context, many=True).data

        return Response(data)

    def list(self, *args, **kwargs):
        ids = list(map(lambda x: int(x), self.request.query_params.getlist('ids[]')))

        if len(ids) > 0:
            response = self._get_by_ids(ids)
        else:
            response = super().list(*args, **kwargs)

        return response
