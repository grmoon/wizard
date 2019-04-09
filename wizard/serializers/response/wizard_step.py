from rest_framework import serializers

from wizard.models import WizardStep
from wizard.serializers.response.step import StepResponseSerializer

class WizardStepResponseSerializer(serializers.ModelSerializer):
    step = serializers.SerializerMethodField()

    class Meta:
        model = WizardStep
        fields = '__all__'

    def get_step(self, wizard_step):
        return StepResponseSerializer(wizard_step.step, context=self.context).data

