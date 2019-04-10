from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from wizard.models import WizardStep
from wizard.response_builders import WizardStepResponseBuilder
from wizard.serializers.model import WizardStepSerializer


class WizardStepViewSet(viewsets.ModelViewSet):
    queryset = WizardStep.objects.all()
    serializer_class = WizardStepSerializer

    def _get_step_for_wizard(self, wizard_id, step_num):
        return Response(WizardStepResponseBuilder.build(self.request.user, wizard_id, step_num))

    def list(self, *args, **kwargs):
        wizard_id = self.request.query_params.get('wizard_id')
        step_num = self.request.query_params.get('step_num')

        if step_num is not None and wizard_id is not None:
            response = self._get_step_for_wizard(int(wizard_id), int(step_num))
        else:
            response = super().list(*args, **kwargs)

        return response