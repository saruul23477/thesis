from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login, name='login'),
    url(r'^(?P<name>[A-Za-z]{0,8})/log/$', views.log, name='log'),

    url(r'^(?P<name>[A-Za-z]{0,8})/video/$', views.video, name='videos'),

]