from django import forms

from .models import Mail

class MailForm(forms.ModelForm):
   class Meta:
     model = Mail
     fields = '__all__'
     labels = {
        'email': 'Email',
        'password': 'Password',
     }
     error_messages = {
       'email': {
         'required': 'Not be empty'
       }
     }
