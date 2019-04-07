from rest_framework import serializers

from wizard.models import SectionQuestion

class SectionQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionQuestion
        fields = '__all__'
