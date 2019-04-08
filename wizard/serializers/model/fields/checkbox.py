from rest_framework import serializers

from wizard.models import CheckboxField, CheckboxFieldOption
from wizard.serializers.model.fields.multiple_choice_field import MultipleChoiceFieldSerializer

class CheckboxFieldSerializer(MultipleChoiceFieldSerializer):
    class Meta:
        model = CheckboxField
        option_model = CheckboxFieldOption
        fields = '__all__'
