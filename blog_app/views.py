from django.shortcuts import render
from django.http import HttpResponse

def blog_home(request):
    return render(request, 'blog_app/index.html')