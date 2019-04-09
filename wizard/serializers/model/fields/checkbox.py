from rest_framework import serializers

from wizard.models import CheckboxField, CheckboxOption
from wizard.serializers.model.fields.multiple_choice import MultipleChoiceFieldSerializer

class CheckboxFieldSerializer(MultipleChoiceFieldSerializer):
    class Meta:
        model = CheckboxField
        option_model = CheckboxOption
        fields = '__all__'
