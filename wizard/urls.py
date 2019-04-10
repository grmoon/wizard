from django.urls import path

from rest_framework.routers import DefaultRouter


from wizard.views import (
    AnswerBulkAPIView,
    AnswerViewSet,
    CheckboxFieldViewSet,
    CheckboxOptionViewSet,
    FieldViewSet,
    MeView,
    OptionViewSet,
    QuestionViewSet,
    RadioButtonFieldViewSet,
    RadioButtonOptionViewSet,
    SectionQuestionViewSet,
    SectionViewSet,
    StepSectionViewSet,
    StepViewSet,
    TextFieldViewSet,
    TriggerViewSet,
    WizardStepViewSet,
    WizardViewSet,
)

router = DefaultRouter()

router.register('answers', AnswerViewSet, basename='answer')
router.register('fields', FieldViewSet, basename='field')
router.register('options', OptionViewSet, basename='option')
router.register('questions', QuestionViewSet, basename='question')
router.register('radio_button_fields', RadioButtonFieldViewSet, basename='radio_button_field')
router.register('radio_button_options', RadioButtonOptionViewSet, basename='radio_button_option')
router.register('checkbox_fields', CheckboxFieldViewSet, basename='checkbox_field')
router.register('checkbox_options', CheckboxOptionViewSet, basename='checkbox_option')
router.register('section_questions', SectionQuestionViewSet, basename='section_question')
router.register('sections', SectionViewSet, basename='section')
router.register('step_sections', StepSectionViewSet, basename='step_section')
router.register('steps', StepViewSet, basename='step')
router.register('text_fields', TextFieldViewSet, basename='text_field')
router.register('triggers', TriggerViewSet, basename='trigger')
router.register('wizard_steps', WizardStepViewSet, basename='wizard_step')
router.register('wizards', WizardViewSet, basename='wizard')

urlpatterns = [
    path('me/', MeView.as_view(), name='me'),
    path('answers/bulk/', AnswerBulkAPIView.as_view(), name='answer.bulk'),
] + router.urls

