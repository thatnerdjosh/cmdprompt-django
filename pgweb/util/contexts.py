from django.template import RequestContext
from django.utils.functional import SimpleLazyObject
from django.conf import settings

# This is the whole site navigation structure. Stick in a smarter file?
sitenav = [
	{'title': 'Home', 'navcontext': 'home', 'link': '/'},
	{'title': 'About', 'navcontext': 'about', 'link':'/about/', 'submenu': [
		{'title': 'Careers', 'link':'/about/careers/'},
		{'title': 'Partners', 'link':'/about/partners/'},
	]},
	{'title': 'Services', 'navcontext': 'services', 'link':'/services/', 'submenu': [
			{'title': 'Audit and Tune', 'link':'/services/auditandtune/'},
			{'title': 'High Availability Clusters', 'link':'/services/highavailabilityclusters'},
			{'title': 'Hot Standby / DRBD', 'link':'/services/hotcoldstandby'},
			{'title': 'Performance Audit', 'link':'/services/performanceaudit'},
			{'title': 'PostgreSQL Core', 'link':'/services/postgresqlcore'},
			{'title': 'Warm Standby', 'link':'/services/warmstandby'},
			{'title': 'Dedicated Hosting', 'link':'/services/dedicatedhosting/'},
			{'title': 'On-Site', 'link':'/services/onsite/'},
			{'title': 'Remote Hands', 'link':'/services/remotehands/'},
			{'title': 'Training', 'link':'/services/training/'},
	]},
	{'title': 'Products', 'navcontext': 'products', 'link':'/products/', 'submenu': [
			{'title': 'Audit and Tune', 'link':'/products/auditandtune/'},
			{'title': 'High Availability Clusters', 'link': '/products/highavailabilityclusters/'},
			{'title': 'Hot Standby / DRBD', 'link': '/products/hotcoldstandby/'},
			{'title': 'Performance Audit', 'link': '/products/performanceaudit/'},
			{'title': 'PostgreSQL Core', 'link': '/products/postgresqlcore/'},
			{'title': 'Warm Standby', 'link': '/products/warmstandby/'}
	]},
	{'title': 'Support', 'navcontext': 'support', 'link':'/support/', 'submenu': [
		{'title': 'Incident Packs', 'link':'/support/incidentpacks/'},
		{'title': 'Support Options', 'link':'/support/supportoptions/'},
		{'title': 'Terms of Service', 'link':'/support/terms/'},
	]},
	{'title': 'Blog', 'navcontext': 'blog', 'link': '/blog/'},
	{'title': 'Contact', 'navcontext': 'contact', 'link': '/contact/'}
]

class NavContext(RequestContext):
	def __init__(self, request, section):
		RequestContext.__init__(self, request)
		self.update({'navmenu': sitenav})
		self.update({'navsection': section})


def _get_gitrev():
	# Return the current git revision, that is used for
	# cache-busting URLs.

	### If there is no master branch known, return 0
	try:
		with open('.git/refs/heads/master') as f:
			return f.readline()[:8]
	except:
		return 0

# Template context processor to add information about the root link and
# the current git revision. git revision is returned as a lazy object so
# we don't spend effort trying to load it if we don't need it (though
# all general pages will need it since it's used to render the css urls)
def PGWebContextProcessor(request):
	gitrev = SimpleLazyObject(_get_gitrev)
	if request.is_secure():
		return {
			'link_root': settings.SITE_ROOT,
			'gitrev': gitrev,
		}
	else:
		return {
			'gitrev': gitrev,
		}
