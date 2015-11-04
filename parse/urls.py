from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^parse/$', views.parse_view, name='parse_view'),
]
