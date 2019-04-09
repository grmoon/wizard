from rest_framework import serializers

from wizard.models import StepSection

class StepSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepSection
        fields = '__all__'
