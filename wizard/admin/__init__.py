from django.contrib import admin

from wizard.admin.fields import (
    RadioButtonFieldAdmin
)
from wizard.models import (
    Answer,
    Question,
    RadioButtonField,
    Option,
    Section,
    Step,
    Trigger,
    Wizard,
)
from wizard.admin.section import SectionAdmin
from wizard.admin.step import StepAdmin
from wizard.admin.wizard import WizardAdmin
from wizard.admin.question import QuestionAdmin

admin.site.register(Answer)
admin.site.register(Question, QuestionAdmin)
admin.site.register(RadioButtonField, RadioButtonFieldAdmin)
admin.site.register(Option)
admin.site.register(Section, SectionAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(Trigger)
admin.site.register(Wizard, WizardAdmin)