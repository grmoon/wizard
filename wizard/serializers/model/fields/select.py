from rest_framework import serializers

from wizard.models import SelectField, SelectOption
from wizard.serializers.model.fields.multiple_choice import MultipleChoiceFieldSerializer

class SelectFieldSerializer(MultipleChoiceFieldSerializer):
    class Meta:
        model = SelectField
        option_model = SelectOption
        fields = '__all__'
