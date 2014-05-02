from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from hotels import views
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hotels/', include('hotels.urls')),

    # Examples:
    url(r'^$', 'vzmm.views.index', name='home'),
    url(r'^about/', 'vzmm.views.about', name='about'),
    url(r'^tos/', 'vzmm.views.tos', name='tos'),
    url(r'^privacy/', 'vzmm.views.privacy', name='privacy'),
    # url(r'^vzmm/', include('vzmm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^api/', include('api.urls')),

)



# SO thread for serving media dir in local 
# http://stackoverflow.com/questions/5517950/django-media-url-and-media-root
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

