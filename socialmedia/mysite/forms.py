from django import forms
from .models import Post, Comment


class NewPostForm(forms.ModelForm):
    """Form for the post model"""

    class Meta:
        model = Post
        fields = ('user', 'title', 'image', 'caption', 'create_date')


class NewCommentForm(forms.ModelForm):
    """Form for the post model"""

    class Meta:
        model = Comment
        fields = ('user', 'comment', 'created_date')
