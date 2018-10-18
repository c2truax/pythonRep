from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index),
        url(r'^create/$', views.create),
        url(r'^success/$', views.success),
        url(r'^read/$', views.read),
        url(r'^success/send/$', views.send),
        url(r'^logout/$', views.logout),
        url(r'^success/comment/$', views.comment),
]
