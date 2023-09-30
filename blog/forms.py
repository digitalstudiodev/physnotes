from django import forms
from .models import Comment, Post, Tag

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'user', 'comment'
        ]
    

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'preview', 'read_time', 'content' ,'tag', 'featured_image','note']
        widgets = {
            'tag': forms.CharField(label='Tag Options', widget=forms.Select(choices=Tag.objects.all()))
        }