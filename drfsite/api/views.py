from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Women
from .permission import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer


class WomenAPIList(generics.ListCreateAPIView):
    """Displays all elements and creates a new element,
    methods GET and POST """
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated,)


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    """Updates a single,
    methods PUT and PATCH"""
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    """Displays a single,
     methods GET, PUT, PATCH and DELETE"""

    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,)
