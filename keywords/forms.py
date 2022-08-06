from django import forms

from .models import Keyword, KeywordGroup

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


class KeywordGroupForm(forms.ModelForm):
  class Meta:
    model = KeywordGroup
    fields = '__all__'
    labels = {
      'keywordgroup': 'Keyword Group',
      'keyword': 'Keyword',
    }
