from django.shortcuts import render_to_response

from pgweb.util.contexts import NavContext

from models import Service, PackageService

def about(request):
    return render_to_response('pages/services.html', {

    }, NavContext(request, 'about'))
