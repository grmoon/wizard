from rest_framework import serializers

from wizard.models import CheckboxOption

class CheckboxOptionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckboxOption
        fields = '__all__'