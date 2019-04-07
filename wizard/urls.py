from rest_framework.routers import DefaultRouter

from wizard.views import (
    AnswerViewSet,
    FieldViewSet,
    OptionViewSet,
    QuestionViewSet,
    RadioButtonFieldViewSet,
    RadioButtonFieldOptionViewSet,
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
router.register('radio_button_field_options', RadioButtonFieldOptionViewSet, basename='radio_button_field_option')
router.register('section_questions', SectionQuestionViewSet, basename='section_question')
router.register('sections', SectionViewSet, basename='section')
router.register('step_sections', StepSectionViewSet, basename='step_section')
router.register('steps', StepViewSet, basename='step')
router.register('text_fields', TextFieldViewSet, basename='text_field')
router.register('triggers', TriggerViewSet, basename='trigger')
router.register('wizard_steps', WizardStepViewSet, basename='wizard_step')
router.register('wizards', WizardViewSet, basename='wizard')

urlpatterns = router.urls