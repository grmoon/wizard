from rest_framework import serializers

from wizard.models import Section, SectionQuestion

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
