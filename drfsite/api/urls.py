from django.urls import path, include, re_path

from api.views import (
    WomenAPIList,
    WomenAPIUpdate,
    WomenAPIDestroy,
)

urlpatterns = [
    path('api/v1/drf-auth/', include('rest_framework.urls')),  # http://127.0.0.1:8000/api/v1/drf-auth/login/
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),  # http://127.0.0.1:8000/api/v1/auth/
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
