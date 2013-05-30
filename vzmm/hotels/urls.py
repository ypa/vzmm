from django.conf.urls import patterns, url

from hotels import views

urlpatterns = patterns('',
    # ex: /hotels/
    url(r'^$', views.index, name='index'),
    # ex: /hotels/3/
    url(r'^(?P<hotel_id>\d+)/$', views.detail, name='detail'),
    # ex: /hotels/classifieds/
    url(r'^classifieds/$', views.classifieds, name='classifieds'),
)