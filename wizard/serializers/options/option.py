from rest_framework import serializers

from wizard.models import Option

class OptionSerializer(serializers.ModelSerializer):
    triggers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
