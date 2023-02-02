from django import forms

class input_url(forms.Form):
    url = forms.CharField(required=True)
    