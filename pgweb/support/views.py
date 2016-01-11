from django.shortcuts import render_to_response

from pgweb.util.contexts import NavContext

from models import SupportPage, SupportPageSection

def support(request):
    support_page = SupportPage.objects.filter(url_slug='/')[0]
    support_sections = SupportPageSection.objects.filter(support_page=support_page)
    return render_to_response('pages/support/page.html', {
        'support_page': support_page,
        'support_sections': support_sections
    }, NavContext(request, 'support'))

def view_page(request, support_page):
    support_page = SupportPage.objects.filter(url_slug=support_page)[0]
    support_sections = SupportPageSection.objects.filter(support_page=support_page)
    return render_to_response('pages/support/page.html', {
        'support_page': support_page,
        'support_sections': support_sections
    }, NavContext(request, 'support'))
