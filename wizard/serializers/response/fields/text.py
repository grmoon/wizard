from rest_framework import serializers

from wizard.models import TextField

class TextFieldResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextField
        fields = '__all__'