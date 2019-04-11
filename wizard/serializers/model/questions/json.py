from rest_framework import serializers

from wizard.models import JSONQuestion, Trigger

class JSONQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JSONQuestion
        fields = '__all__'