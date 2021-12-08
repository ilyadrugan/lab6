from rest_framework import serializers

from news.models import Category
class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    name_eng = serializers.CharField(max_length=255)

    class Meta:
        model = Category
        fields =[
            'id', 'name', 'name_eng'
        ]