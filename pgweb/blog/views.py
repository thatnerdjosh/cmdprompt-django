from django.shortcuts import render_to_response
from models import BlogPost
from pgweb.util.contexts import NavContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404

def all_posts(request, page=1):
    blog_post = BlogPost.objects.all()
    paginator = Paginator(blog_post, 25)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render_to_response('pages/blog/all.html', {
        'posts': posts,
    }, NavContext(request, 'blog'))

def by_slug(request, blog):
    blog_post = BlogPost.objects.filter(url_slug=blog)[0]

    response = render_to_response('pages/blog/post.html', {
	    'blog_post': blog_post,
    }, NavContext(request, 'blog'))

    if not blog_post:
        raise Http404

    return response
