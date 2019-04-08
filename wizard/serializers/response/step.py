from rest_framework import serializers

from wizard.models import Step, StepSection
from wizard.serializers.response.through.step_section import StepSectionResponseSerializer

class StepResponseSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()

    class Meta:
        model = Step
        fields = '__all__'

    def get_sections(self, step):
        step_sections = StepSection.objects.filter(step=step)

        return StepSectionResponseSerializer(step_sections, many=True, context=self.context).data