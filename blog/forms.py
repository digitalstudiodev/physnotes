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
        tag_names= []
        for tag in Tag.objects.all():
            tag_names.append(tag.tag_name)
        widgets = {
            'tag': forms.MultipleChoiceField( required=True, widget=forms.RadioSelect(), choices=Tag.objects.all())
        }