from django.shortcuts import render
from .models import News
from .models import Category

def GetNews(request, id):
    return render(request, 'main/news.html', {'data' : {
        'news': News.objects.filter(category_id=id),
        # 'bzu': News.objects.filter(fruit_id=id)[0],
        'categories': Category.objects.all(),
        'category': Category.objects.filter(id=id),
    }})

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {'data' : {
        'categories': Category.objects.all()
    }})

