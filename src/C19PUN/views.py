from django.http import HttpResponse
from django.shortcuts import render

def my_home_page(request):
	#return HttpResponse("Hello World")
	return render(request, 'home.html')
def about(request):
	#return HttpResponse("about")
	return render(request, 'about.html')
#def test_list(request):
#	return render(request, 'test/test_list.html')