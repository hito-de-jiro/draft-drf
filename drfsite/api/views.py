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
            # post_new = Women.objects.create(
            #     title=request.data['title'],
            #     content=request.data['content'],
            #     category_id=request.data['category_id'],
            # )
            serializer.save()

            # return Response({'title': WomenSerializer(post_new).data}, status=status.HTTP_201_CREATED)
            return Response({'title': serializer.data}, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        if not pk:
            return Response({'error': 'Method PUT not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data}, status=status.HTTP_201_CREATED)


