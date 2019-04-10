from rest_framework import serializers


class GenericSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        if hasattr(obj, 'content_object'):
            content_object = obj.content_object
        else:
            content_object = obj

        content_object_class = content_object.__class__
        serializer = self.SERIALIZERS[content_object_class]
        data = serializer(content_object, context=self.context).data
        data['class'] = content_object_class.__name__

        return data

