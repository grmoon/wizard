from rest_framework import serializers

from wizard.models import StepSection
from wizard.serializers.response.section import SectionResponseSerializer

class StepSectionResponseSerializer(serializers.ModelSerializer):
    section = serializers.SerializerMethodField()

    class Meta:
        model = StepSection
        fields = '__all__'

    def get_section(self, step_section):
        return SectionResponseSerializer(step_section.section, context=self.context).data
