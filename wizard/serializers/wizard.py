from rest_framework import serializers

from wizard.models import Wizard

class WizardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wizard
        fields = '__all__'
