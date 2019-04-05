from django.contrib import admin

from wizard.admin.fields import (
    RadioButtonFieldAdmin
)
from wizard.models import (
    Answer,
    RadioButtonField,
    RadioButtonOption,
    Question,
    Trigger,
)

admin.site.register(Answer)
admin.site.register(Trigger)
admin.site.register(RadioButtonField, RadioButtonFieldAdmin)
admin.site.register(RadioButtonOption)
admin.site.register(Question)