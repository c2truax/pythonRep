from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^$', views.index),
		url(r'^create/$', views.create),
		url(r'^dashboard/$', views.dashboard),
		url(r'^jobs/new/$', views.new),
		url(r'^createjob/$', views.createjob),
		url(r'^jobs/edit/(?P<id>\d+)/$', views.edit),
		url(r'^editjob/(?P<id>\d+)/$', views.editjob),
		url(r'^jobs/(?P<id>\d+)/$', views.viewjob),
		url(r'^addjob/(?P<id>\d+)/$', views.addjob),
		url(r'^deletejob/(?P<id>\d+)/$', views.deletejob),
		url(r'^donejob/(?P<id>\d+)/$', views.donejob),
		url(r'^contact/(?P<id>\d+)/$', views.contact),
		url(r'^danger/$', views.danger),
		url(r'^about/$', views.about),
		url(r'^email/$', views.email),
		url(r'^get_involved/$', views.get_involved),
		url(r'^logout/$', views.logout),
		url(r'^read/$', views.read)
]