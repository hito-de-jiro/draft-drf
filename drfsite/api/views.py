from rest_framework import generics

from .models import Women
from .serializers import WomenSerializer


class WomenAPIList(generics.ListCreateAPIView):
    """Displays all elements and creates a new element,
    methods GET and POST """
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIUpdate(generics.UpdateAPIView):
    """Updates a single,
    methods PUT and PATCH"""
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Displays a single,
     methods GET, PUT, PATCH and DELETE"""
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
