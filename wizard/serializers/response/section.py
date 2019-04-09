from rest_framework import serializers

from wizard.models import Section, SectionQuestion
from wizard.serializers.response.through.section_question import SectionQuestionResponseSerializer

class SectionResponseSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Section
        fields = '__all__'

    def get_questions(self, section):
        section_questions = SectionQuestion.objects.filter(section=section)

        return SectionQuestionResponseSerializer(section_questions, many=True, context=self.context).data
