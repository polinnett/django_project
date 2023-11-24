from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from calory_counter import settings
from main.views import VegetableAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('api/v1/veglist', VegetableAPIView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

