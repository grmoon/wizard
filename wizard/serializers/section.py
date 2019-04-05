from rest_framework import serializers

from wizard.models import Section

class SectionSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Section
        fields = '__all__'
