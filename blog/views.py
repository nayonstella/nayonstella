from django.shortcuts import render
from blog.models import Post
# Create your views here.
def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {
        'post_list': post_list,
        })

def detail(request, pk):
    post_list = Post.obejcts.all()
    return render(request, 'blog/index.html', {
        'post_list': post_list
        })