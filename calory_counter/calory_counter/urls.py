from django.contrib import admin
from django.conf.urls.static import static
from django.template.defaulttags import url
from django.urls import path, include, re_path

from calory_counter import settings
from main.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'veg', VegetableViewSet, basename='veg')
# router.register(r'fruit', FruitViewSet, basename='fru')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('api/v1/', include(router.urls)),
    path('api/v1/proflist/', ProfileAPIList.as_view()),
    path('api/v1/proflist/<int:pk>', ProfileAPIDestroy.as_view()),
    re_path('api/v1/record/(?P<veg_id>.+)/$', RecordAPIList.as_view()),
    path('api/v1/record/', RecordQueryAPIList.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

