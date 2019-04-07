from rest_framework import serializers

from wizard.models import Trigger

class TriggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trigger
        fields = '__all__'
