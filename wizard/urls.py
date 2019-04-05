from rest_framework.routers import DefaultRouter

from wizard.views import (
    AnswerViewSet,
    RadioButtonFieldViewSet,
    RadioButtonOptionViewSet,
    QuestionViewSet,
)

router = DefaultRouter()

router.register('answers', AnswerViewSet, basename='answer')
router.register('radio_button_fields', RadioButtonFieldViewSet, basename='radio_button_field')
router.register('radio_button_options', RadioButtonOptionViewSet, basename='radio_button_option')
router.register('questions', QuestionViewSet, basename='question')

urlpatterns = router.urls