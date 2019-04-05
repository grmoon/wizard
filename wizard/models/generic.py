from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class GenericModel(models.Model):
    content_object = GenericForeignKey('content_type', 'id')
    content_type = models.ForeignKey(ContentType, blank=False, on_delete=models.CASCADE, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.content_type_id:
            self.content_type_id = ContentType.objects.get_for_model(self.__class__).pk

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.content_object)
