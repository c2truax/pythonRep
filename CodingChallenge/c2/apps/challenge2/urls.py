from django.urls import path

from . import views

app_name = 'c2'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('<int:uid>/edit', views.edit, name='edit'),
    path('<int:uid>/delete', views.destroy),
    path('<int:uid>', views.update),
]
