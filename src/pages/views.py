from django.shortcuts import render, redirect
from .models import Page
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from .import forms

# Create your views here.

def pages_list(request):
	allpages = Page.objects.all().order_by('date')
	return render(request, 'pages/pages_list.html',{'allpages':allpages})

#query the database to find an article based on the slug.
#if it exisit we grab it send it back to the template to display the article.

def article_detail(request, slug):
	#return HttpResponse(slug)
	pagearticle = Page.objects.get(slug=slug)
	return render(request, 'pages/pages_details.html', {'mypage':pagearticle})

#this is protecting this view below. User needs to be logged in. to see the create page.

@login_required(login_url="/accounts/login")
def page_create(request):
#when we click on create button this is what its going to do.
	if request.method == 'POST':
		form = forms.CreateArticle(request.POST, request.FILES)
		if form.is_valid():
#we need to save the article based on the user. Who created this article ? this will be done below using foreign key.
			
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect('pages:list')
	else:
		form = forms.CreateArticle()
	return render(request, 'pages/page_create.html', {'form': form})