from rest_framework import serializers

from wizard.models import SelectField, SelectOption
from wizard.serializers.response.fields.multiple_choice import MultipleChoiceFieldResponseSerializer

class SelectFieldResponseSerializer(MultipleChoiceFieldResponseSerializer):
    class Meta:
        model = SelectField
        option_model = SelectOption
        fields = '__all__'
