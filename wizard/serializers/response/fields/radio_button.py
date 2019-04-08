from wizard.models import RadioButtonField, RadioButtonFieldOption
from wizard.serializers.response.fields.multiple_choice_field import MultipleChoiceFieldResponseSerializer

class RadioButtonFieldResponseSerializer(MultipleChoiceFieldResponseSerializer):
    class Meta:
        model = RadioButtonField
        option_model = RadioButtonFieldOption
        fields = '__all__'