from rest_framework import serializers

from wizard.models import FileQuestion, Trigger

class FileQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileQuestion
        fields = '__all__'