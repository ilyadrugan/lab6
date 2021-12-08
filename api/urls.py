from django.urls import path, include
from .views_api import CategoryListAPIView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'Categories', CategoryListAPIView)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]