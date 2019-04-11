import json

from rest_framework import authentication
from rest_framework.response import Response
from rest_framework.views import APIView

from wizard.models import Upload
from wizard.serializers import UploadSerializer


class UploadBulkAPIView(APIView):
    authentication_classes = (authentication.SessionAuthentication,)

    def delete(self, request):
        upload_ids = request.query_params.getlist('upload_ids[]')
        uploads = Upload.objects.filter(pk__in=upload_ids).all()

        data = UploadSerializer(uploads, many=True).data
        uploads.delete()

        return Response(data)