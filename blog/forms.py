from django import forms

from .models import Blog

class BlogForm(forms.ModelForm):
   class Meta:
     model = Blog
     fields = '__all__'
     labels = {
        'email': 'Email',
        'blog': 'Blog',
        'email_post': 'Email Post',
     }
     error_messages = {
        'email': {
            'required': 'Not be empty'
        },
        'blog': {
            'required': 'Not be empty'
        },
        'email_post': {
            'required': 'Not be empty'
        },
     }
