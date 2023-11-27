from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from calory_counter import settings
from main.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'veg', VegetableViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('api/v1/', include(router.urls)),
    # path('api/v1/veglist/', VegetableViewSet.as_view({'get': 'list'})),
    # path('api/v1/veglist/<int:pk>', VegetableViewSet.as_view({'put': 'update'}))
    # path('api/v1/vegdetail/<int:pk>', VegetableAPIDetailView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

