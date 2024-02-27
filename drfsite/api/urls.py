from django.urls import path, include

from api.views import (
    # WomenAPIList,
    # WomenAPIUpdate,
    # WomenAPIDetailView,
    WomenViewSet,
)

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'women', WomenViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls))
    # path('v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
    # path('v1/womenlist/', WomenAPIList.as_view()),
    # path('v1/womenlist/<int:pk>/', WomenAPIUpdate.as_view()),
    # path('v1/womendetail/<int:pk>/', WomenAPIDetailView.as_view()),
]
