from rest_framework import serializers

from wizard.models import Question, Trigger

class QuestionSerializer(serializers.ModelSerializer):
    field_class = serializers.CharField(source='field.content_type.model')
    triggers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = '__all__'

    def get_triggers(self, from_question, **kwargs):
        return Trigger.objects.filter(from_question=from_question).values_list('pk', flat=True)