from django import forms
from .models import post
from ckeditor.widgets import CKEditorWidget

class Postform(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(),label='Text Editor')
    
    class Meta:
        model = post
        fields = ('body',)