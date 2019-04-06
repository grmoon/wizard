from rest_framework import serializers

from wizard.models import SectionQuestion
from wizard.serializers.question import QuestionSerializer

class SectionQuestionSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = SectionQuestion
        fields = '__all__'
