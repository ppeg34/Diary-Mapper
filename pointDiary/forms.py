from django import forms

class PointForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    lat = forms.CharField()
    lng = forms.CharField()
