from wizard.models import RadioButtonField, RadioButtonOption
from wizard.serializers.model.fields.multiple_choice import MultipleChoiceFieldSerializer

class RadioButtonFieldSerializer(MultipleChoiceFieldSerializer):
    class Meta:
        model = RadioButtonField
        option_model = RadioButtonOption
        fields = '__all__'