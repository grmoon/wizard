from rest_framework import serializers

from wizard.models import Question, Trigger

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'