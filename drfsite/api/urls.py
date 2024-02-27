from django.urls import path

from api.views import (
    WomenAPIList,
    WomenAPIUpdate,
    WomenAPIDetailView,
)

urlpatterns = [
    path('v1/womenlist/', WomenAPIList.as_view()),  # GET and POST requests
    path('v1/womenlist/<int:pk>/', WomenAPIUpdate.as_view()),  # PUT and PATCH requests
    path('v1/womendetail/<int:pk>/', WomenAPIDetailView.as_view()),  # GET and POST requests
]
