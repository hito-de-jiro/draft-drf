from django.urls import path

from api.views import (
    WomenAPIList,
    WomenAPIUpdate,
    WomenAPIDestroy,
)

urlpatterns = [
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
]
