from django.contrib import admin
from django.urls import path
from blog_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', views.blog_index, name="blog-index"),
    path('newpost/', views.new_post, name='new_post'),
]