from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create/$', views.create),
    url(r'^confirmation/(?P<id>\d+)/$', views.confirmation),
    url(r'^destroy/$', views.destroy),
]