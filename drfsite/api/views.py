from django.forms import model_to_dict
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer


# class WomanApiView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

class WomanApiView(APIView):
    def get(self, request):
        women = Women.objects.all().values()
        return Response({'post': WomenSerializer(women, many=True).data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            post_new = Women.objects.create(
                title=request.data['title'],
                content=request.data['content'],
                category_id=request.data['category_id'],
            )
            return Response({'title': WomenSerializer(post_new).data}, status=status.HTTP_201_CREATED)
