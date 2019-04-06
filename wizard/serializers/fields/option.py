from rest_framework import serializers

from wizard.models import Option

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'