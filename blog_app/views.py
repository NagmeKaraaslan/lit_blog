from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


class PostListView(ListView):
    model = Post
    template_name = 'blog_app/main.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

def home(request):
    return render(request, 'blog_app/index.html')

def blog_index(request):
    return render(request, 'blog/index.html')

def main_page(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog_app/main.html', {'post':posts})

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('main_page')
    else:
        form = PostForm()
    return render(request, 'blog_app/newpost.html', {'form': form})

def newpost_view(request):
    return render(request,'blog_app/newpost.html')

def main_page(request):
    return render(request, 'blog_app/main.html')