from rest_framework import serializers

from wizard.models import CheckboxOption

class CheckboxOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckboxOption
        fields = '__all__'
