from django import forms
from .models import Post, Image, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content',]

        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ('post', )
        widgets = {
            'file': forms.FileInput(attrs={'multiple':True}),
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)