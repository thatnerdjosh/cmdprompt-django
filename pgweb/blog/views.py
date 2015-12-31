from django.shortcuts import render_to_response
from models import BlogPost
from pgweb.util.contexts import NavContext
from django.http import Http404

def by_slug(request, blog):
    blog_post = BlogPost.objects.filter(url_slug=blog)[0]

    response = render_to_response('pages/blog/post.html', {
	    'blog_post': blog_post,
    }, NavContext(request, 'blog'))

    if not blog_post:
        raise Http404

    return response
