from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Post
from .forms import PostForm
from django.http import HttpResponseBadRequest, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth.decorators import login_required


class PostListView(ListView):
    model = Post
    template_name = 'blog_app/main.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

def main_page(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog_app/main.html', {'post':posts})

from django.views.decorators.csrf import csrf_protect

@csrf_protect
def new_post(request):
    if request.method == 'POST':
        try:
            if request.content_type=='application/json':
                data = json.loads(request.body)
                if not data.get('content'):
                    return JsonResponse({'error':'Bir şey yazmadan göndermeye çalışıyorsunuz.'},status=400)
                post = Post.objects.create(
                    title=data.get('title', ''),
                    content=data['content']
                )
                return JsonResponse({'success': True, 'post_id': post.id})
            else:
                form = PostForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('blog_app:main_page')
                return HttpResponseBadRequest("Form geçersiz")
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Geçersiz JSON verisi'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    form = PostForm()
    return render(
        request,
        'blog_app/newpost.html',
        {'form': form}
    )