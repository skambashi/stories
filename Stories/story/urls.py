from django.conf.urls import patterns, url
from story import views

urlpatterns = patterns(
    '', # Let's not forget this...
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^new_story/', views.new_story, name='new_story'),
    url(r'^(?P<story_id>\d+)/$', views.view_story, name='view_story'),
)