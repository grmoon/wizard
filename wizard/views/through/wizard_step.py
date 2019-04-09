from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from wizard.models import WizardStep
from wizard.serializers import WizardStepResponseSerializer


class WizardStepViewSet(viewsets.ModelViewSet):
    queryset = WizardStep.objects.all()
    serializer_class = WizardStepResponseSerializer

    def _get_step_for_wizard(self, wizard_id, step_num):
        try:
            step = self.queryset\
                .filter(wizard_id=wizard_id)\
                .order_by('position')[step_num - 1]
        except (AssertionError, IndexError):
            raise NotFound()
        else:
            context = { 'request': self.request }
            return Response(WizardStepResponseSerializer(step, context=context).data)

    def list(self, *args, **kwargs):
        wizard_id = self.request.query_params.get('wizard_id')
        step_num = self.request.query_params.get('step_num')

        if step_num is not None and wizard_id is not None:
            response = self._get_step_for_wizard(int(wizard_id), int(step_num))
        else:
            response = super().list(*args, **kwargs)

        return response