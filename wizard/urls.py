from rest_framework.routers import DefaultRouter

from wizard.views import (
    AnswerViewSet,
    RadioButtonFieldViewSet,
    RadioButtonOptionViewSet,
    QuestionViewSet,
    TriggerViewSet,
    SectionViewSet,
    StepViewSet,
)

router = DefaultRouter()

router.register('answers', AnswerViewSet, basename='answer')
router.register('radio_button_fields', RadioButtonFieldViewSet, basename='radio_button_field')
router.register('radio_button_options', RadioButtonOptionViewSet, basename='radio_button_option')
router.register('questions', QuestionViewSet, basename='question')
router.register('triggers', TriggerViewSet, basename='trigger')
router.register('sections', SectionViewSet, basename='section')
router.register('steps', StepViewSet, basename='step')

urlpatterns = router.urls