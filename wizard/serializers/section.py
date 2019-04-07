from rest_framework import serializers

from wizard.models import Section, SectionQuestion

class SectionSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Section
        fields = '__all__'

    def get_questions(self, section, **kwargs):
        return SectionQuestion.objects.filter(section=section).values_list('pk', flat=True)
