from rest_framework import serializers

from wizard.models import RadioButtonOption

class RadioButtonOptionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadioButtonOption
        fields = '__all__'