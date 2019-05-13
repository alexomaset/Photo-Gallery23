from . import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static


urlpatterns=[
  
     url('^$', views.day_photos, name='day_photos'),
     url(r'^image/(\d+)',views.image,name ='image'),
     url(r'^search/', views.search_results, name='search_results'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 