from rest_framework import serializers

from wizard.models import Option
from wizard.serializers.generic import GenericSerializer
from wizard.serializers.model.options.option import OptionSerializer
from wizard.serializers.response.options.checkbox import (
    CheckboxOption,
    CheckboxOptionResponseSerializer,
)
from wizard.serializers.response.options.radio_button import (
    RadioButtonOption,
    RadioButtonOptionResponseSerializer,
)
from wizard.serializers.response.options.select import (
    SelectOption,
    SelectOptionResponseSerializer,
)

class OptionResponseSerializer(GenericSerializer):
    SERIALIZERS = {
        CheckboxOption: CheckboxOptionResponseSerializer,
        RadioButtonOption: RadioButtonOptionResponseSerializer,
        SelectOption: SelectOptionResponseSerializer,
    }

    class Meta:
        model = Option
        fields = '__all__'

    def to_representation(self, option):
        data = super().to_representation(option)
        data['option'] = OptionSerializer(option.option, context=self.context).data

        return data