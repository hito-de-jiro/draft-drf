from django.urls import path, include, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from api.views import (
    WomenAPIList,
    WomenAPIUpdate,
    WomenAPIDestroy,
)

urlpatterns = [
    path('women/', WomenAPIList.as_view()),
    path('women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
    path('auth/', include('djoser.urls')),
    # http://127.0.0.1:8000/api/v1/auth    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
