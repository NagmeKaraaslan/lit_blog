from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('new-post/', views.new_post, name='new_post'),
]
