from wizard.models import RadioButtonField, RadioButtonFieldOption
from wizard.serializers.fields.multiple_choice_field import MultipleChoiceFieldSerializer

class RadioButtonFieldSerializer(MultipleChoiceFieldSerializer):
    class Meta:
        model = RadioButtonField
        option_model = RadioButtonFieldOption
        fields = '__all__'