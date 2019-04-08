from rest_framework import serializers

from wizard.models import WizardStep

class WizardStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = WizardStep
        fields = '__all__'
