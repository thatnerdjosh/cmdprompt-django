from django.shortcuts import render_to_response

from pgweb.util.contexts import NavContext

from models import TeamMember, AboutContentBlock, Career

def about(request):
    team_members = TeamMember.objects.all
    content_top = AboutContentBlock.objects.filter(position=AboutContentBlock.TOP)
    content_bottom = AboutContentBlock.objects.filter(position=AboutContentBlock.BOTTOM)
    return render_to_response('pages/about.html', {
	    'team_members': team_members,
        'content_top': content_top,
        'content_bottom': content_bottom
    }, NavContext(request, 'about'))


def careers(request):
    careers = Career.objects.all
    return render_to_response('pages/about/careers.html', {
	    'careers': careers,
    }, NavContext(request, 'about'))

def partners(request):
    return render_to_response('pages/about/partners.html', {
    }, NavContext(request, 'about'))
