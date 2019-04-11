from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


from website.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('api/v1/', include('wizard.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
