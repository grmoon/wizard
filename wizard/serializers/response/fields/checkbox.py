from rest_framework import serializers

from wizard.models import CheckboxField, CheckboxOption
from wizard.serializers.response.fields.multiple_choice import MultipleChoiceFieldResponseSerializer

class CheckboxFieldResponseSerializer(MultipleChoiceFieldResponseSerializer):
    class Meta:
        model = CheckboxField
        option_model = CheckboxOption
        fields = '__all__'
