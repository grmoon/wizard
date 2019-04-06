from rest_framework import serializers

from wizard.models import RadioButtonFieldOption
from wizard.serializers.fields.option import OptionSerializer

class RadioButtonFieldOptionSerializer(serializers.ModelSerializer):
    option = OptionSerializer()

    class Meta:
        model = RadioButtonFieldOption
        fields = '__all__'
