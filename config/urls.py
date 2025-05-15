from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog_app.urls')),
    path('new/', views.new_post, name='new_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)