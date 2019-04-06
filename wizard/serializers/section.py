from wizard.models import Section, StepSection
from wizard.serializers.position import PositionSerializer

class SectionSerializer(PositionSerializer):
    class Meta:
        model = Section
        fields = '__all__'

        outer_id = 'step_id'
        inner_model_key = 'section'
        outer_model = StepSection
