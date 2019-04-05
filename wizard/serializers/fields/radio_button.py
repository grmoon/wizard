from rest_framework import serializers

from wizard.models import RadioButtonField

class RadioButtonFieldSerializer(serializers.ModelSerializer):
    options = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = RadioButtonField
        fields = '__all__'