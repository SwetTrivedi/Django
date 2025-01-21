from django import forms
class Studentregistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()