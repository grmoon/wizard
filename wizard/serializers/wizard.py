from rest_framework import serializers

from wizard.models import Wizard, WizardStep

class WizardSerializer(serializers.ModelSerializer):
    steps = serializers.SerializerMethodField()
    class Meta:
        model = Wizard
        fields = '__all__'

    def get_steps(self, wizard, **kwargs):
        return WizardStep.objects.filter(wizard=wizard).values_list('pk', flat=True)
