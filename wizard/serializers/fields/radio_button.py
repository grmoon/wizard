from rest_framework import serializers

from wizard.models import RadioButtonField

class RadioButtonFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadioButtonField
        fields = '__all__'