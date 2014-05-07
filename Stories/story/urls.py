from django.conf.urls import patterns, url
from story import views

urlpatterns = patterns(
    '', # Let's not forget this...
    url(r'^$', views.index, name='index'),
    url(r'^(?P<story_id>\d+)/$', views.story, name='view_story'),
)