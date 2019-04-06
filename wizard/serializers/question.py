from rest_framework import serializers

from wizard.models import Answer, Question, Trigger

class QuestionSerializer(serializers.ModelSerializer):
    answer = serializers.SerializerMethodField()
    field = serializers.PrimaryKeyRelatedField(read_only=True)
    field_class = serializers.CharField(source='field.content_type.model')
    triggers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = '__all__'

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