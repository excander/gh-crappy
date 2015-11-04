from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index_view, name='index_view'),
]
