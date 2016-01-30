from django.conf.urls import *

urlpatterns = patterns('',
    (r'^(?P<name>.+)/(?P<page>\d+)/$', 'pgweb.blog.views.by_category'),
    (r'^(?P<name>.+)/$', 'pgweb.blog.views.by_category'),
)

