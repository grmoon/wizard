from rest_framework import serializers

from wizard.models import SectionQuestion
from wizard.serializers.response.question import QuestionResponseSerializer

class SectionQuestionResponseSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()

    class Meta:
        model = SectionQuestion
        fields = '__all__'

    def get_question(self, section_question):
        return QuestionResponseSerializer(section_question.question, context=self.context).data
