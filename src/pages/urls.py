from django.urls import path
from . import views

#name spacing the url by giving the name to the app.

app_name = 'pages'

urlpatterns = [
	path('',views.pages_list, name='list'),
	path('create/',views.page_create, name='create'),
	#This url is for article_details page. & In this below line we captured the slug and sent it  back via httpresponse definied in views.py of this app.
	#to understnd the URL pattern refer to https://docs.djangoproject.com/en/3.0/topics/http/urls/
	path('<slug:slug>/',views.article_detail, name='page_detail'),
]




