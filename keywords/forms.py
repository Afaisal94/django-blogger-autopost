from django import forms

from .models import Keyword

class KeywordForm(forms.ModelForm):
   class Meta:
     model = Keyword
     fields = '__all__'
     labels = {
        'keyword': 'Keyword',
     }
     error_messages = {
       'keyword': {
         'required': 'Not be empty'
       }
     }
