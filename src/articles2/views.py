from django.shortcuts import render
from .models import Articles
from django.http import HttpResponse

# Create your views here.

def articles_list(request):
	Article = Articles.objects.all().order_by('date')
	return render(request, 'articles/articles_list.html',{ 'Article': Article })
    

def article_detail(request, slug):
	return HttpResponse(slug)
	#article = Articles.objects.get(slug=slug)
	#return render(request, 'articles/article_detail.html',{'Articles': article})

