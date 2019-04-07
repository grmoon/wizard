from rest_framework import serializers

from wizard.models import (
    Field,
    RadioButtonField,
    TextField
)
from wizard.serializers.fields.radio_button import RadioButtonFieldSerializer
from wizard.serializers.fields.text import TextFieldSerializer

class FieldSerializer(serializers.ModelSerializer):
    SERIALIZERS = {
        RadioButtonField: RadioButtonFieldSerializer,
        TextField: TextFieldSerializer
    }

    class Meta:
        model = Field
        fields = '__all__'

    def to_representation(self, field):
        content_object = field.content_object
        content_object_class = content_object.__class__
        serializer = self.SERIALIZERS[content_object_class]
        data = serializer(content_object, context=self.context).data
        data['class'] = content_object_class.__name__

        return data

