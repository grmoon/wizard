from rest_framework import serializers


class PositionSerializer(serializers.ModelSerializer):
    position = serializers.SerializerMethodField()

    @classmethod
    def _get_outer_id(cls, request):
        return None if request is None else request.query_params.get(cls.Meta.outer_id)

    @classmethod
    def _get_position(cls, outer_id, model):
        if outer_id is not None:
            try:
                params = {}
                params[cls.Meta.outer_id] = outer_id
                params[cls.Meta.inner_model_key] = model

                instance = cls.Meta.outer_model.objects.get(**params)
            except cls.Meta.outer_model.DoesNotExist:
                position = None
            else:
                position = instance.position
        else:
            position = None

        return position

    def get_position(self, step):
        request = self.context.get('request')
        outer_id = self._get_outer_id(request)
        position = self._get_position(outer_id, step)

        return position
