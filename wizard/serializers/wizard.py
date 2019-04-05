from rest_framework import serializers

from wizard.models import Wizard

class WizardSerializer(serializers.ModelSerializer):
    steps = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Wizard
        fields = '__all__'
