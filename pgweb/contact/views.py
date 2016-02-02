from django.shortcuts import redirect, render_to_response
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage

from pgweb.util.contexts import NavContext

from models import ContactSection
from forms import ContactForm

def contact(request):
        contact_form = ContactForm
        form = contact_form
        if request.method == "POST":
            form = contact_form(data=request.POST)

            if form.is_valid():
                contact_name = request.POST.get(
                    'contact_name'
                , '')
                contact_email = request.POST.get(
                    'contact_email'
                , '')
                form_content = request.POST.get('content', '')

                # Email the profile with the 
                # contact information
                template = get_template('contact_template.txt')
                context = Context({
                    'contact_name': contact_name,
                    'contact_email': contact_email,
                    'form_content': form_content,
                })
                content = template.render(context)

                email = EmailMessage(
                    "New contact form submission",
                    content,
                    contact_email,
                    ['sales@commandprompt.com'],
                    headers = {'Reply-To': contact_email }
                )
                email.send()
        
        contact_sections = ContactSection.objects.all()
        return render_to_response('pages/contact.html', {
            'contact_sections': contact_sections,
            'form': form
        }, NavContext(request, 'contact'))
 
