from django.urls import path

from website.views import IndexView

urlpatterns = [
    path('done/', IndexView.as_view(), name='done'),
    path('wizard/<wizard_id>/step/<step_num>/', IndexView.as_view(), name='wizard_step')
]
