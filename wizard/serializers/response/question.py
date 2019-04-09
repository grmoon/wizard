from rest_framework import serializers

from wizard.models import Question, Trigger, Answer
from wizard.serializers.response.fields.field import FieldResponseSerializer
from wizard.serializers.response.trigger import TriggerResponseSerializer
from wizard.serializers.model.answer import AnswerSerializer

class QuestionResponseSerializer(serializers.ModelSerializer):
    field = serializers.SerializerMethodField()
    triggers = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = '__all__'

    def get_answer(self, question):
        user = self.context['request'].user

        try:
            answer = Answer.objects.get(question=question, user=user)
        except Answer.DoesNotExist:
            data = None
        else:
            data = AnswerSerializer(answer, context=self.context).data

        return data

    def get_field(self, question):
        return FieldResponseSerializer(question.field, context=self.context).data

    def get_triggers(self, question):
        triggers = Trigger.objects.filter(from_question=question)

        return TriggerResponseSerializer(triggers, many=True, context=self.context).data
