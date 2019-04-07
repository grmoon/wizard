from rest_framework import serializers

from wizard.models import CheckboxFieldOption
from wizard.serializers.fields.option import OptionSerializer

class CheckboxFieldOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckboxFieldOption
        fields = '__all__'
