from rest_framework import serializers

from wizard.models import Answer, Question

class QuestionSerializer(serializers.ModelSerializer):
    answer = serializers.SerializerMethodField()
    field = serializers.PrimaryKeyRelatedField(read_only=True)
    field_class = serializers.CharField(source='field.content_type.model')

    class Meta:
        model = Question
        fields = '__all__'

    def get_answer(self, question):
        user = self.context['request'].user

        try:
            answer = question.answers.get(user=user)
        except Answer.DoesNotExist:
            answer_id = None
        else:
            answer_id = answer.pk

        return answer_id