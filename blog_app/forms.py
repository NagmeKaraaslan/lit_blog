from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'content' : forms.Textarea(attrs={
                'class': 'Başlık girmek ister misin ?',
                'rows': 5,
                'placeholder': 'İçeriğinizi yazın.',
            })
        }
        labels = {
            'title':'',
            'contenet':'',
        }
        