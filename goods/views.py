from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FoodCategory, FoodListSerializer


class FoodCategoryListView(APIView):

    def get(self, request, *args, **kwargs):

        categories = FoodCategory.objects.filter(food__is_publish=True).distinct()
        serializer = FoodListSerializer(categories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
