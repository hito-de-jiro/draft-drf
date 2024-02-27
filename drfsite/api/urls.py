from django.urls import path

from api.views import (
    # WomenAPIList,
    # WomenAPIUpdate,
    # WomenAPIDetailView,
    WomenViewSet,
)


urlpatterns = [
    # path('v1/womenlist/', WomenAPIList.as_view()),
    # path('v1/womenlist/<int:pk>/', WomenAPIUpdate.as_view()),
    # path('v1/womendetail/<int:pk>/', WomenAPIDetailView.as_view()),
    path('v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    path('v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
]
