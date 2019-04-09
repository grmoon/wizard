from rest_framework import serializers

from wizard.models import CheckboxFieldOption

class CheckboxFieldOptionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckboxFieldOption
        fields = '__all__'