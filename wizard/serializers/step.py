from wizard.models import Step, WizardStep
from wizard.serializers.position import PositionSerializer

class StepSerializer(PositionSerializer):
    class Meta:
        model = Step
        fields = '__all__'

        outer_id = 'wizard_id'
        inner_model_key = 'step'
        outer_model = WizardStep
