from django.template import RequestContext
from django.utils.functional import SimpleLazyObject
from django.conf import settings

# This is the whole site navigation structure. Stick in a smarter file?
from pgweb.services.models import Service
from pgweb.products.models import Product
from pgweb.support.models import SupportPage
from pgweb.blog.models import BlogPost

class NavContext(RequestContext):
	def __init__(self, request, section):
		RequestContext.__init__(self, request)
		services = Service.objects.all()

		service_url_list = []
		for service in services:
			service_url_list.append({'title': service.name, 'link': '/services/' + service.url_slug})

		products = Product.objects.all()

		product_url_list = []
		for product in products:
			product_url_list.append({'title': product.name, 'link': '/products/' + product.url_slug})

		support_pages = SupportPage.objects.all()

		support_page_list = []
		for page in support_pages:
			if page.url_slug != "/":
				support_page_list.append({'title': page.name, 'link': '/support/' + page.url_slug})

		sitenav = [
			{'title': 'Home', 'navcontext': 'home', 'link': '/'},
			{'title': 'About', 'navcontext': 'about', 'link':'/about/', 'submenu': [
				{'title': 'Careers', 'link':'/about/careers/'},
				{'title': 'Partners', 'link':'/about/partners/'},
			]},
			{'title': 'Products', 'navcontext': 'products', 'link':'/products/', 'submenu': product_url_list},
			{'title': 'Services', 'navcontext': 'services', 'link':'/services/', 'submenu': service_url_list},
			{'title': 'Support', 'navcontext': 'support', 'link':'/support/', 'submenu': support_page_list},
			{'title': 'Blog', 'navcontext': 'blog', 'link': '/blog/'},
			{'title': 'Contact', 'navcontext': 'contact', 'link': '/contact/'}
		]

                posts = BlogPost.objects.all()
                
                self.update({'products': products})
                self.update({'services': services})
                self.update({'blogposts': posts})
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
