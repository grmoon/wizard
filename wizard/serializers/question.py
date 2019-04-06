from rest_framework import serializers

from wizard.models import Answer, Question, Trigger, SectionQuestion
from wizard.serializers.position import PositionSerializer

class QuestionSerializer(PositionSerializer):
    answer = serializers.SerializerMethodField()
    field = serializers.PrimaryKeyRelatedField(read_only=True)
    field_class = serializers.CharField(source='field.content_type.model')
    triggers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = '__all__'

        outer_id = 'section_id'
        inner_model_key = 'question'
        outer_model = SectionQuestion

    def get_triggers(self, question):
        return Trigger.objects.filter(from_question=question).values_list('pk', flat=True)

    def get_answer(self, question):
        user = self.context['request'].user

        try:
            answer = question.answers.get(user=user)
        except Answer.DoesNotExist:
            answer_id = None
        else:
            answer_id = answer.pk

        return answer_id