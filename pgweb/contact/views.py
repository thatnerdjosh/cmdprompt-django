from django.shortcuts import render_to_response

from pgweb.util.contexts import NavContext

from models import ContactSection

def contact(request):
    contact_sections = ContactSection.objects.all()
    return render_to_response('pages/contact.html', {
        'contact_sections': contact
    }, NavContext(request, 'contact'))
