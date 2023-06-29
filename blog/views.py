from django.shortcuts import render, redirect
from django.utils.text import slugify
from .models import Post
from .forms import PostForm
import random
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.

def frontpage(request):
    newest_posts = Post.objects.all()[0:8]
    return render(request, 'frontpage.html',{'newest_posts': newest_posts})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()

            return redirect('frontpage')
    else:
        form = PostForm()

    return render(request, 'add_post.html', {'form': form})

def post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    return render(request, 'post.html', {'post': post})
