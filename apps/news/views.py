from django.shortcuts import render
from apps.base.models import Settings
from apps.news.models import News

# Create your views here.
def news(request):
    settings = Settings.objects.latest('id')
    news = News.objects.all()
    return render(request, "blog/blog.html", locals())

def news_detail(request, id):
    settings = Settings.objects.latest('id')
    new = News.objects.get(id=id)
    return render(request, "blog/blog-details.html", locals())



def news(request):
    settings = Settings.objects.latest('id')
    news = News.objects.all()
    return render(request, "blog/blog.html", locals())

def news_detail(request, id):
    settings = Settings.objects.latest('id')
    new = News.objects.get(id=id)
    return render(request, "blog/blog-details.html", locals())