from django.urls import path

from api.views import WomenAPIList

urlpatterns = [
    path('v1/womenlist/', WomenAPIList.as_view()),  # GET and POST requests
]
