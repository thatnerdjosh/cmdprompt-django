from django.conf.urls import *
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

# Register our save signal handlers
from pgweb.util.bases import register_basic_signal_handlers
register_basic_signal_handlers()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


# dict with all the RSS feeds we can serve
from core.feeds import VersionFeed
from news.feeds import NewsFeed
from events.feeds import EventFeed
from pwn.feeds import PwnFeed

urlpatterns = patterns('',
    (r'^$', 'pgweb.core.views.home'),
    (r'^dyncss/(?P<css>base|docs).css$', 'pgweb.core.views.dynamic_css'),


	(r'^robots.txt$', 'pgweb.core.views.robots'),

    ###
    # RSS feeds
    ###
    #(r'^versions.rss$', VersionFeed()),

    ###
    # Special sections
    ###

    #ABOUT
    (r'^about/', include('pgweb.about.urls')),
    (r'^blog/', include('pgweb.blog.urls')),
    
    ###
	# Sitemap (FIXME: support for >50k urls!)
	###
	(r'^sitemap.xml', 'pgweb.core.views.sitemap'),

    url(r'^tinymce/', include('tinymce.urls')),
    ###
    # Workaround for broken links pushed in press release
    ###
    (r'^downloads/$', RedirectView.as_view(url='/download/')),

    # Some basic information about the connection (for debugging purposes)
	(r'^system_information/$', 'pgweb.core.views.system_information'),

    # API endpoints
    (r'^api/varnish/purge/$', 'pgweb.core.views.api_varnish_purge'),

    # Pingback from git repo to update site
    (r'^api/repo_updated/$', 'pgweb.core.views.api_repo_updated'),

	# Override some URLs in admin, to provide our own pages
	(r'^admin/pending/$', 'pgweb.core.views.admin_pending'),
	(r'^admin/purge/$', 'pgweb.core.views.admin_purge'),
	(r'^admin/mergeorg/$', 'pgweb.core.views.admin_mergeorg'),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # This should not happen in production - serve by the webserver natively!
    url(r'^(favicon.ico)$', 'django.views.static.serve', {
        'document_root': '../static',
    }),

    # Crash testing URL :-)
    (r'^crashtest/$', 'pgweb.misc.views.crashtest'),

	# If we're getting an attempt for something ending in HTML, just get rid of it
	(r'^(.*)\.html$', 'pgweb.legacyurl.views.html_extension'),

    # Fallback for static pages, must be at the bottom
    (r'^(.*)/$', 'pgweb.core.views.fallback'),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
    )

