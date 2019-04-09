from rest_framework import serializers

from wizard.models import CheckboxField, CheckboxFieldOption
from wizard.serializers.response.fields.multiple_choice_field import MultipleChoiceFieldResponseSerializer

class CheckboxFieldResponseSerializer(MultipleChoiceFieldResponseSerializer):
    class Meta:
        model = CheckboxField
        option_model = CheckboxFieldOption
        fields = '__all__'
