from rest_framework import serializers

from wizard.models import JSONAnswer

class JSONAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = JSONAnswer
        fields = '__all__'