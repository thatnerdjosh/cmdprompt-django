from django.conf.urls import *
from django.views.generic import RedirectView

# Register our save signal handlers
from pgweb.util.bases import register_basic_signal_handlers
register_basic_signal_handlers()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #(r'^$', 'pgweb.blog.views.all_posts'),
    (r'^(?P<blog>^[a-zA-Z].*)/$', 'pgweb.blog.views.by_slug'),
)
