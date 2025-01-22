from django import forms
class Studentregistration(forms.Form):
    name=forms.CharField(label='name',label_suffix=' ',initial='swet',required=False)
    # name=forms.CharField(widget=forms.PasswordInput())

class Back(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()

class Fields(forms.Form):
    name=forms.CharField(min_length=2,max_length=5,strip=False, error_messages={'required':'please enter your name'},
                         empty_value='swet')
    roll=forms.IntegerField(max_value=50)
    agree=forms.BooleanField()

