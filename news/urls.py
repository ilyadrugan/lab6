from django.urls import path, include
from . import views

# from rest_framework import routers
# from api.views_api import FruitListAPIView


urlpatterns = [
    path('', views.index, name='home'),
    path('api/', include('api.urls')),
    path('category/<int:id>/', views.GetNews, name='category_url')
]