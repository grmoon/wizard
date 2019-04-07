from django.urls import path

from website.views import IndexView

urlpatterns = [
    path('wizard/<wizard_id>/step/<step_num>/', IndexView.as_view(), name='index')
]
