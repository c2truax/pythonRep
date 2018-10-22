from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^$', views.index),
		url(r'^create/$', views.create),
		url(r'^books/$', views.books),
		url(r'^books/(?P<id>\d+)/$', views.view_book),
		url(r'^users/(?P<id>\d+)/$', views.user_review),
		url(r'^books/add/$', views.add),
		url(r'^compute_add/$', views.compute_add),
		url(r'^compute_review/$', views.compute_review),
		url(r'^logout/$', views.logout),
		url(r'^delete/(?P<id>\d+)$', views.delete),
		url(r'^read/$', views.read)
]