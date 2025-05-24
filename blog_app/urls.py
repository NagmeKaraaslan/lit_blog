from django.urls import path
from . import views
from .views import PostListView, new_post

app_name = 'blog_app'

urlpatterns = [
    path('', PostListView.as_view(), name='main_page'),
    path('new-post/', views.new_post, name='new_post'),
]
