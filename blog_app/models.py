from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

user = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField("Oluşturulma tarihi", auto_now_add=True)
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    updated_at = models.DateTimeField("Güncellenme tarihi", auto_now=True)
    """  like_count = models.PositiveIntegerField("Beğeni Sayısı", default=0)
    comment_count = models.PositiveIntegerField("Yorum Sayısı", default=0) """


    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Eser'
        verbose_name_plural = 'Eserler'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_Detail', kwargs={'pk': self.pk})