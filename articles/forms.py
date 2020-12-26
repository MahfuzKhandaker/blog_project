from django import forms
from .models import Article, Comment


class JoinForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=120)


# class ArticleForm(forms.ModelForm):
#     description = forms.CharField(
#         widget=forms.Textarea(attrs={
#         'placeholder': 'Write your blog here...',
#         'required': False, 
#         'cols': 30, 
#         'rows': 10
#     })
#     )

    class Meta:
        model = Article
        fields = ('title', 'description',)


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Leave a comment!',
        'id': 'comment-text',
        'rows': '4'
    }))
    class Meta:
        model = Comment
        fields = ['text']