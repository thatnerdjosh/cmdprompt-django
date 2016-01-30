from django.shortcuts import render_to_response

from pgweb.util.contexts import NavContext

from models import Product, ProductSection, ProductFeatureGrid, ProductFeatureGridObject
from django.http import Http404

def products(request):
    products = Product.objects.all()

    return render_to_response('pages/products.html', {
	    'products': products
    }, NavContext(request, 'products'))

def view_product(request, product):
    product = Product.objects.filter(url_slug=product)[0]
    feature_grids = ProductFeatureGrid.objects.filter(product=product)
    feature_grid_listings = []
    for feature_grid in feature_grids:
        feature_grid_objects = ProductFeatureGridObject.objects.filter(feature_grid=feature_grid)
        feature_grid_listings.append(feature_grid_objects)

    if not product:
        raise Http404

    return render_to_response('pages/products/product.html', {
	    'product': product,
        'feature_grid_listings': feature_grid_listings
    }, NavContext(request, 'products'))
