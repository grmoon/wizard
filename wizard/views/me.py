from django.http import JsonResponse
from django.views import View

from wizard.serializers import UserSerializer

class MeView(View):
    def get(self, request):
        data = UserSerializer(request.user).data

        return JsonResponse(data)