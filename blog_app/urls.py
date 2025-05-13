from django.urls import path
from . import views

urlpatterns= [
    path('main/', views.main_page, name='blog_main'),
    path( 'newpost/', views.new_post, name='newpost'),
]