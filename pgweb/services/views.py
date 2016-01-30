from django.shortcuts import render_to_response

from pgweb.util.contexts import NavContext

from models import Service, ServiceSection, PackageService, ProfessionalService, CloudService

def services(request):
    packageServices = PackageService.objects.all
    professionalServices = ProfessionalService.objects.all
    cloudServices = CloudService.objects.all
    return render_to_response('pages/services.html', {
        'packageServices': packageServices,
        'professionalServices': professionalServices,
        'cloudServices': cloudServices
    }, NavContext(request, 'services'))

def view_service(request, service):
    service_result = Service.objects.filter(url_slug=service)[0]
    sections = ServiceSection.objects.filter(service=service_result)

    if not service_result:
        raise Http404

    return render_to_response('pages/services/info.html', {
        'service': service_result,
        'sections': sections
    }, NavContext(request, 'services'))
