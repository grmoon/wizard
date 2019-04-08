from rest_framework import serializers

from wizard.models import Option
from wizard.serializers.generic import GenericSerializer
from wizard.serializers.model.options.option import OptionSerializer
from wizard.serializers.response.options.checkbox import (
    CheckboxFieldOption,
    CheckboxFieldOptionResponseSerializer,
)
from wizard.serializers.response.options.radio_button import (
    RadioButtonFieldOption,
    RadioButtonFieldOptionResponseSerializer,
)

class OptionResponseSerializer(GenericSerializer):
    SERIALIZERS = {
        CheckboxFieldOption: CheckboxFieldOptionResponseSerializer,
        RadioButtonFieldOption: RadioButtonFieldOptionResponseSerializer,
    }

    class Meta:
        model = Option
        fields = '__all__'

    def to_representation(self, option):
        data = super().to_representation(option)
        data['option'] = OptionSerializer(option.option, context=self.context).data

        return data