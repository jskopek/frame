from django.conf.urls import patterns, include, url
from db_storage.views import ImageView

urlpatterns = patterns('',
    url(r'^(?P<file_name>[^/]+)$', ImageView.as_view(), name='db_storage_image'),
) 
