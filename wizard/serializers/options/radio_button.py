from wizard.serializers.options.option import OptionSerializer
from wizard.models import RadioButtonOption

class RadioButtonOptionSerializer(OptionSerializer):
    class Meta:
        model = RadioButtonOption
        fields = '__all__'