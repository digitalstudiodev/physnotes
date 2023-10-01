from django import forms
from .models import Comment, Post, Tag, ContentCat

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
            'tag': forms.SelectMultiple(choices=tuple(list(Tag.objects.all())))
        }

class TagForm(forms.ModelForm):
    
    class Meta:
        model = Tag
        fields = ['tag_name', 'category']

        widgets = {
            'category': forms.SelectMultiple(choices=tuple(list(ContentCat.objects.all())))
        }