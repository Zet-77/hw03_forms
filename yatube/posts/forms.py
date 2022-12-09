from django import forms

from .models import Post, Group


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
        
        