from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'content' : forms.Textarea(attrs={
                'class': 'yeni içerik',
                'rows': 5,
                'placeholder': 'Yeni yazım:',
            })
        }
        labels = {
            'title':'',
            'contenet':'',
        }
        