from wizard.models import Field
from wizard.serializers.generic import GenericSerializer
from wizard.serializers.model.fields.checkbox import CheckboxField, CheckboxFieldSerializer
from wizard.serializers.model.fields.radio_button import RadioButtonField, RadioButtonFieldSerializer
from wizard.serializers.model.fields.text import TextField, TextFieldSerializer

class FieldSerializer(GenericSerializer):
    SERIALIZERS = {
        CheckboxField: CheckboxFieldSerializer,
        RadioButtonField: RadioButtonFieldSerializer,
        TextField: TextFieldSerializer,
    }

    class Meta:
        model = Field
        fields = '__all__'
