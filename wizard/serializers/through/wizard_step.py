from rest_framework import serializers

from wizard.models import WizardStep
from wizard.serializers.step import StepSerializer

class WizardStepSerializer(serializers.ModelSerializer):

    class Meta:
        model = WizardStep
        fields = '__all__'
