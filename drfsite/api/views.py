from rest_framework import viewsets, mixins, generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Women, Category
from .serializers import WomenSerializer


class WomenAPIList(generics.ListCreateAPIView):
    """Displays all elements and creates a new element,
    methods GET and POST """
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated,)


class WomenAPIUpdate(generics.UpdateAPIView):
    """Updates a single,
    methods PUT and PATCH"""
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    """Displays a single,
     methods GET, PUT, PATCH and DELETE"""

    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminUser,)

