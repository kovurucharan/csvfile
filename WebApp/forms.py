from django import forms
from WebApp.models import Uploadfile

class Uploadfileform(forms.ModelForm):
    class Meta:
        model=Uploadfile
        fields='__all__'