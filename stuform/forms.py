from django import forms
from django.core import validators

#this is modelform import 
from . models import User
# This class is label tag uses


class Studentregistration(forms.Form):
    name=forms.CharField(label='name',label_suffix=' ',required=False)
    email=forms.EmailField()
# ,initial='swet'
# widget=forms.PasswordInput()
# This class is redirect uses method 1 and method 2

class Back(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()

# This class is form fields uses

class Fields(forms.Form):
    name=forms.CharField(min_length=2,max_length=5,strip=False, error_messages={'required':'please enter your name'}
                         ,empty_value='swet')
    roll=forms.IntegerField(max_value=50)
    agree=forms.BooleanField()

# This is cleaning and validating specific fields method 1.

class Student1(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    def clean_name(self):
        valname=self.cleaned_data['name']
        if len(valname)< 4:
            raise forms.ValidationError('Please Enter the  name graeter than four ')
        return valname


# This is clean nad validate method 2
class Student2(forms.Form):
     name=forms.CharField()
     email=forms.EmailField()
     def clean(self):
        cleaned_data=super().clean()
        valname=self.cleaned_data['name']
        if len(valname)< 4:
            raise forms.ValidationError('Please Enter the  name graeter than four ')
        valemail=self.cleaned_data['email']
        if len(valemail)< 7:
            raise forms.ValidationError('Please Enter the email graeter than Seven ')

     


# This is builtin validators 
class builtin(forms.Form):
    name=forms.CharField(validators=[validators.MaxLengthValidator(2)])
    email=forms.EmailField()




# This is match password class                                                                            


class match(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Password(again)',widget=forms.PasswordInput)
    def clean(self):
        self.cleaned_data=super().clean()
        valpwd=self.cleaned_data['password']
        valrpwd=self.cleaned_data['rpassword']
        if valpwd!=valrpwd:
            raise forms.ValidationError('Password not match ')



# THis class is save the data in database nin admin panal. 
class Saving(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)


#This is a model form page .
class Modelform(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        labels={'name':'Enter Name'}
        error_massage={'name':{'required':'Write Your Name'}}
        widgets={'password':forms.PasswordInput,'name':forms.TextInput(attrs={'placeholder':'Enter your name'})}

