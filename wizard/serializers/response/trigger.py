from rest_framework import serializers

from wizard.models import Trigger

class TriggerResponseSerializer(serializers.ModelSerializer):
    to_question = serializers.SerializerMethodField()

    class Meta:
        model = Trigger
        fields = '__all__'

    @classmethod
    def _get_question_response_serializer(cls):
        if not hasattr(cls, 'QuestionResponseSerializer'):
            from wizard.serializers.response.question import QuestionResponseSerializer

            cls.QuestionResponseSerializer = QuestionResponseSerializer

        return cls.QuestionResponseSerializer

    def get_to_question(self, trigger):
        QuestionResponseSerializer = self._get_question_response_serializer()

        return QuestionResponseSerializer(trigger.to_question, context=self.context).data

