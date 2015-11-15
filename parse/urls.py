from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^parse/$', views.parse_view, name='parse_view'),
    url(r'^parse/start-parse$', views.start_parse, name='start_parse'),
    url(r'^parse/static/result_file.xls', views.download_file, name='download_file'),
    url(r'^parse/(?P<infield>.+)/$', views.parse_result, name='parse_result'),
]
