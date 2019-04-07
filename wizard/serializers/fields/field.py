from wizard.models import Field
from wizard.serializers.fields.checkbox import CheckboxField, CheckboxFieldSerializer
from wizard.serializers.fields.radio_button import RadioButtonField, RadioButtonFieldSerializer
from wizard.serializers.fields.text import TextField, TextFieldSerializer
from wizard.serializers.generic import GenericSerializer

class FieldSerializer(GenericSerializer):
    SERIALIZERS = {
        CheckboxField: CheckboxFieldSerializer,
        RadioButtonField: RadioButtonFieldSerializer,
        TextField: TextFieldSerializer,
    }

    class Meta:
        model = Field
        fields = '__all__'
