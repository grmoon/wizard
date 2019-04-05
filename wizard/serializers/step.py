from rest_framework import serializers

from wizard.models import Step

class StepSerializer(serializers.ModelSerializer):
    sections = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Step
        fields = '__all__'
