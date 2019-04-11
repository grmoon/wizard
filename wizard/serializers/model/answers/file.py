from rest_framework import serializers

from wizard.models import FileAnswer

class FileAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileAnswer
        fields = '__all__'