from rest_framework import serializers

from wizard.models import Question

class QuestionSerializer(serializers.ModelSerializer):
    field = serializers.PrimaryKeyRelatedField(read_only=True)
    field_class = serializers.CharField(source='field.content_type.model')

    class Meta:
        model = Question
        fields = '__all__'