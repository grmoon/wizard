from rest_framework import serializers

from wizard.models import FileField

class FileFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileField
        fields = '__all__'