from wizard.models import MultipleChoiceOption
from wizard.serializers.generic import GenericSerializer
from wizard.serializers.model.options.radio_button import (
    RadioButtonOption,
    RadioButtonOptionSerializer,
)
from wizard.serializers.model.options.checkbox import (
    CheckboxOption,
    CheckboxOptionSerializer,
)
from wizard.serializers.model.options.select import (
    SelectOption,
    SelectOptionSerializer,
)

class MultipleChoiceOptionSerializer(GenericSerializer):
    SERIALIZERS = {
        CheckboxOption: CheckboxOptionSerializer,
        RadioButtonOption: RadioButtonOptionSerializer,
        SelectOption: SelectOptionSerializer,
    }

    class Meta:
        model = MultipleChoiceOption
        fields = '__all__'
