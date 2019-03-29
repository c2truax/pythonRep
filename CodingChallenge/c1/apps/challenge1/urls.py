from django.urls import path

from . import views

app_name = 'c1'

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register),
    path('dashboard', views.dashboard, name='dashboard'),
    path('users/<int:uid>', views.show),
    path('login', views.login),
    path('logout', views.logout),
]
