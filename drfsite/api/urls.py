from django.urls import path, include

from api.views import (
    # WomenAPIList,
    # WomenAPIUpdate,
    # WomenAPIDetailView,
    WomenViewSet,
)

from rest_framework import routers


class MyCustomRouter(routers.SimpleRouter):
    routes = [
        routers.Route(
            url=r'^{prefix}/$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        routers.Route(
            url=r'^{prefix}/{lookup}/$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        )
    ]


router = MyCustomRouter()
router.register(r'women', WomenViewSet, basename='women')
print(router.urls)

urlpatterns = [
    path('api/v1/', include(router.urls))
    # path('v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
    # path('v1/womenlist/', WomenAPIList.as_view()),
    # path('v1/womenlist/<int:pk>/', WomenAPIUpdate.as_view()),
    # path('v1/womendetail/<int:pk>/', WomenAPIDetailView.as_view()),
]
