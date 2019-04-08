from rest_framework import serializers

from wizard.models import MultipleChoiceField, MultipleChoiceFieldOption
from wizard.serializers.response.options.option import OptionResponseSerializer

class MultipleChoiceFieldResponseSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()

    def get_options(self, field, *args, **kwargs):
        options = self.Meta.option_model.objects.filter(field=field)

        return OptionResponseSerializer(options, many=True, context=self.context).data
