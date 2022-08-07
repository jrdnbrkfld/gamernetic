from .models import Comment, Post, User
from django.contrib.auth.forms import UserChangeForm
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm (forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'excerpt', 'slug', 'featured_image',
                  'content', 'author')

        widgets = {
            'title': forms.TextInput(attrs={'placeholder':
                                            'Give it a catchy title'}),
            'excerpt': forms.TextInput(attrs={'placeholder':
                                              'E.g. My first ever post'}),
            'slug': forms.TextInput(attrs={'placeholder':
                                           'E.g. this-is-my-post'}),
            'content': forms.Textarea(attrs={'placeholder':
                                             '<p>Wrap your content in these P tags to create a paragraph</p>\n\n<b>Wrap your words in these B tags to make them bold</b>'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
        }


class EditProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
        widgets = {
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
        }
