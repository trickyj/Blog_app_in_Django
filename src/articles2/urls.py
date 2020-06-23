from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('articles2/',views.articles_list, name="article"),
 	path('articles2/<slug:slug>/',views.article_detail, name="detail"),
]
