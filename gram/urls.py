from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^new/image$', views.new_image, name='new-post'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^like/(\d+)', views.like_image, name='like'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)