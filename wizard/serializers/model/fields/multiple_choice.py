from rest_framework import serializers

from wizard.models import MultipleChoiceField, MultipleChoiceOption

class MultipleChoiceFieldSerializer(serializers.ModelSerializer):
    # options = serializers.SerializerMethodField()

    # def get_options(self, field, *args, **kwargs):
    #     return self.Meta.option_model.objects.filter(field=field).values_list('pk', flat=True)
    pass
