from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/$', views.new),
    url(r'^create/$', views.create),
    url(r'^(?P<num>[0-9]{1,5})/$', views.show),
    url(r'^(?P<num>[0-9]{1,5})/edit/$', views.edit),
    url(r'^(?P<num>[0-9]{1,5})/delete/$', views.destroy),
]