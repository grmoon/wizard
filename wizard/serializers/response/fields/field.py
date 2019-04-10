from wizard.models import Field
from wizard.serializers.generic import GenericSerializer
from wizard.serializers.response.fields.checkbox import CheckboxField, CheckboxFieldResponseSerializer
from wizard.serializers.response.fields.radio_button import RadioButtonField, RadioButtonFieldResponseSerializer
from wizard.serializers.response.fields.text import TextField, TextFieldResponseSerializer
from wizard.serializers.response.fields.select import SelectField, SelectFieldResponseSerializer

class FieldResponseSerializer(GenericSerializer):
    SERIALIZERS = {
        CheckboxField: CheckboxFieldResponseSerializer,
        RadioButtonField: RadioButtonFieldResponseSerializer,
        SelectField: SelectFieldResponseSerializer,
        TextField: TextFieldResponseSerializer,
    }

    class Meta:
        model = Field
        fields = '__all__'
