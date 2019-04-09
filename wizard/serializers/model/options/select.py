from rest_framework import serializers

from wizard.models import SelectOption

class SelectOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectOption
        fields = '__all__'
