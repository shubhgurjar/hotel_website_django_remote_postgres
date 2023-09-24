# forms.py

from django import forms

class CustomerData(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=100, required=True)
    message = forms.CharField(max_length=1000, widget=forms.Textarea, required=True)
