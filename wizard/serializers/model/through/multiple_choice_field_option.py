from wizard.models import MultipleChoiceFieldOption
from wizard.serializers.generic import GenericSerializer
from wizard.serializers.model.through.radio_button_field_option import (
    RadioButtonFieldOption,
    RadioButtonFieldOptionSerializer,
)
from wizard.serializers.model.through.checkbox_field_option import (
    CheckboxFieldOption,
    CheckboxFieldOptionSerializer,
)

class MultipleChoiceFieldOptionSerializer(GenericSerializer):
    SERIALIZERS = {
        CheckboxFieldOption: CheckboxFieldOptionSerializer,
        RadioButtonFieldOption: RadioButtonFieldOptionSerializer,
    }

    class Meta:
        model = MultipleChoiceFieldOption
        fields = '__all__'
