from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

class PostListView(ListView):
    model = Posttemplate_name = 'blog_app/main.html'
    context_object_name = 'posts'
    order,ng = ['-created_at']

#@login_required def new_post(request)


def blog_home(request):
    return render(request, 'blog_app/index.html')

def main(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog_app/main.html', {'post':posts})

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('main')
        else:
            form = PostForm()
        return render(request, 'blog_App/main.html', {'form': form})