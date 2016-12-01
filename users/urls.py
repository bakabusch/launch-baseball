from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),#login form
    url(r'^logout/$', views.logout_view, name='logout'),#logout form
    url(r'^register/$', views.register, name='register'),#registration form
]
