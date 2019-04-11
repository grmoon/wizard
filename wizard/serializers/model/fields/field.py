from wizard.models import Field
from wizard.serializers.generic import GenericSerializer
from wizard.serializers.model.fields.checkbox import CheckboxField, CheckboxFieldSerializer
from wizard.serializers.model.fields.radio_button import RadioButtonField, RadioButtonFieldSerializer
from wizard.serializers.model.fields.select import SelectField, SelectFieldSerializer
from wizard.serializers.model.fields.text import TextField, TextFieldSerializer
from wizard.serializers.model.fields.file import FileField, FileFieldSerializer

class FieldSerializer(GenericSerializer):
    SERIALIZERS = {
        CheckboxField: CheckboxFieldSerializer,
        FileField: FileFieldSerializer,
        RadioButtonField: RadioButtonFieldSerializer,
        SelectField: SelectFieldSerializer,
        TextField: TextFieldSerializer,
    }
