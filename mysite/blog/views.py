from django.shortcuts import render
from django.http import Http404

from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blog/list.html',
                  {
                      'posts': posts,
                  }
                  )

def post_detail(request):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404('No Post Found')

    return render(
        request,
        'blog/post/detail.html',
        {
            'post': post
        }
    )
