from rest_framework import serializers

from wizard.models import Question, Trigger
from wizard.serializers.response.fields.field import FieldResponseSerializer
from wizard.serializers.response.trigger import TriggerResponseSerializer

class QuestionResponseSerializer(serializers.ModelSerializer):
    field = serializers.SerializerMethodField()
    triggers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = '__all__'

    def get_field(self, question):
        return FieldResponseSerializer(question.field, context=self.context).data

    def get_triggers(self, question):
        triggers = Trigger.objects.filter(from_question=question)

        return TriggerResponseSerializer(triggers, many=True, context=self.context).data
