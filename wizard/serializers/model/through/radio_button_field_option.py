from rest_framework import serializers

from wizard.models import RadioButtonFieldOption

class RadioButtonFieldOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadioButtonFieldOption
        fields = '__all__'
