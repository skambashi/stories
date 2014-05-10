from django.conf.urls import patterns, include, url

from django.contrib import admin

from story.views import index

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Stories.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index, name='index'),
    url(r'^story/', include('story.urls', namespace='story')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^key/', include(admin.site.urls)), # admin site
)
