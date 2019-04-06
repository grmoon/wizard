from rest_framework import serializers

from wizard.models import StepSection
from wizard.serializers.section import SectionSerializer

class StepSectionSerializer(serializers.ModelSerializer):
    section = SectionSerializer()

    class Meta:
        model = StepSection
        fields = '__all__'
