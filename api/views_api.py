from rest_framework import viewsets
from news.models import Category
from .serializers import CategorySerializer

class CategoryListAPIView(viewsets.ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
