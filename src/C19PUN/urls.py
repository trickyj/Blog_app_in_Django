from django.contrib import admin
from django.urls import include, path
from . import views
#from .views import my_home_page, about #test_list
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from pages import views as page_views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('pages/', include('pages.urls')),
	path('accounts/', include('accounts.urls')),
	#path('', include(('articles2.urls', 'articles2'), namespace='article')),
	path('',page_views.pages_list, name='home'), 
	path('about/',views.about, name='about'),
	#path('test/',test_list, name='test'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)