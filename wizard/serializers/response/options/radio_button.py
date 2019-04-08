from rest_framework import serializers

from wizard.models import RadioButtonFieldOption

class RadioButtonFieldOptionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadioButtonFieldOption
        fields = '__all__'