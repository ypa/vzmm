from django.conf.urls import patterns, url

from api import views

urlpatterns = patterns('',
    url(r'^email/$', views.email_tour, name='email'),
)