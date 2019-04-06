from rest_framework import serializers

from wizard.models import Step, StepSection


class StepSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()

    class Meta:
        model = Step
        fields = '__all__'

    def get_sections(self, step, **kwargs):
        return StepSection.objects.filter(step=step).values_list('pk', flat=True)