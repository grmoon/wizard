from wizard.models import RadioButtonField, RadioButtonOption
from wizard.serializers.response.fields.multiple_choice import MultipleChoiceFieldResponseSerializer

class RadioButtonFieldResponseSerializer(MultipleChoiceFieldResponseSerializer):
    class Meta:
        model = RadioButtonField
        option_model = RadioButtonOption
        fields = '__all__'