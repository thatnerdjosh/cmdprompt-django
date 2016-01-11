from django.conf.urls import *
from django.views.generic import RedirectView

# Register our save signal handlers
from pgweb.util.bases import register_basic_signal_handlers
register_basic_signal_handlers()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'pgweb.support.views.support'),
    (r'^(?P<support_page>^[a-zA-Z].*)/$', 'pgweb.support.views.view_page'),
)
