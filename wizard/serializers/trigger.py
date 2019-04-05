from rest_framework import serializers

from wizard.models import Trigger

class TriggerSerializer(serializers.ModelSerializer):
    option = serializers.PrimaryKeyRelatedField(read_only=True)
    question = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Trigger
        fields = '__all__'
