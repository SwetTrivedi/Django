from django.shortcuts import render
from  . forms import Studentregistration
from . forms import Fields
from . forms import Back
from . forms import Student1
from . forms import builtin
from . forms import match
from . forms import Saving
from . models import Lame
from . forms import Student2
from . forms import Modelform
from . forms import Modelform1
from django.http import HttpResponseRedirect
# Create your views here.
def thanku(request):
    return render(request,'sucess.html')



def show(request):
    fm=Studentregistration()
    fm.order_fields(field_order=['email','name'])
    return render (request,'registration.html',{'form':fm})

# this is give the output in terminal

def get(request):
    if request.method=='POST':
        fm=Back(request.POST)
        # print(fm)
        # print("This is a post method")
        if fm.is_valid():
            print("Name",fm.cleaned_data['name'])
            print("email",fm.cleaned_data['email'])
            fm=Back() 
    else:
        fm=Back()
        print("This is a get method")
    return render(request,'registration.html',{'form':fm})



# this is a redirect code first method

def redirect1(request):
    if request.method=='POST':
        fm=Back(request.POST)
        if fm.is_valid():
            print("Name",fm.cleaned_data['name'])
            print("email",fm.cleaned_data['email'])
            return render (request,'sucess.html')
    else:
        fm=Studentregistration()
        print("This is a get method")
    return render(request,'registration.html',{'form':fm})


# thisb is redirect code second method
def redirect2(request):
    if request.method=='POST':
        fm=Back(request.POST)
        if fm.is_valid():
            print("Name",fm.cleaned_data['name'])
            print("email",fm.cleaned_data['email'])
            return HttpResponseRedirect('/sucess/')
    else:
        fm=Back()
        print("This is a get method")
    return render(request,'registration.html',{'form':fm})


#  This is form fields usegs

def built(request):
    if request.method=='POST':
        fm=Fields(request.POST)
        if fm.is_valid():
            print('Name:',fm.cleaned_data['name'])
            print('Agree:',fm.cleaned_data['agree'])
    else:
        fm=Fields()
    return render(request,'registration.html',{'form':fm})



# This is method cleaning and validating specifice field method 1
def cleanvalidate1(request):
    if request.method=='POST':
        fm=Student1(request.POST)
        if fm.is_valid():
            print("Name:" ,fm.cleaned_data['name'])
            print("Email:",fm.cleaned_data['email'])
    else:
        fm=Student1()
    return render(request,'registration.html',{'form':fm})

# This is method cleaning and validating specifice field method 2


def cleanvalidate2(request):
    if request.method=='POST':
        fm=Student2(request.POST)
        if fm.is_valid():
            print("Name : ",fm.cleaned_data['name'])
            print('Email :',fm.cleaned_data['email'])
    else:
        fm=Student2()
    return render (request,'registration.html',{'form':fm})



# This is built in validators method

def builtinvalidate(request):
    if request.method=='POST':
        fm=builtin(request.POST)
        if fm.is_valid():
            print("Name:" ,fm.cleaned_data['name'])
            print("Email:",fm.cleaned_data['email'])
    else:
        fm=builtin()
    return render(request,'registration.html',{'form':fm})


# Tjis is match password function


def matching(request):
    if request.method=='POST':
        fm=match(request.POST)
        if fm.is_valid():
            print("Name:" ,fm.cleaned_data['name'])
            print("Email:",fm.cleaned_data['email'])
            print("Password:",fm.cleaned_data['password'])
            print("RPassword:",fm.cleaned_data['rpassword'])
    else:
        fm=match()
    return render(request,'registration.html',{'form':fm})





# This method is how to save dta in admin
def saved(request):
    if request.method=='POST':
        fm=Saving(request.POST)
        if fm.is_valid():
           nm=fm.cleaned_data['name']
           em=fm.cleaned_data['email']
           pw=fm.cleaned_data['password']
           reg=Lame(name=nm,email=em,password=pw)
           reg.save()

    else:
        fm=Saving()
    return render(request,'registration.html',{'form':fm})


#This is use mo0del form 


def md(request):
    if request.method=='POST':
        pi=Lame.objects.get(pk=6)
        fm=Modelform(request.POST,instance=pi )
        if fm.is_valid():
            fm.save()
            # print("Name:" ,fm.cleaned_data['name'])
            # print("Email:",fm.cleaned_data['email'])
            # print("Password:",fm.cleaned_data['password'])

    else:
        fm=Modelform()
    return render(request,'registration.html',{'form':fm})


def md1(request):
    if request.method=='POST':
        fm=Modelform1(request.POST)
        if fm.is_valid():
            print("Name:" ,fm.cleaned_data['name'])
            print("Email:",fm.cleaned_data['email'])
            print("Password:",fm.cleaned_data['password'])


    else:
        fm=Modelform1()
    return render(request,'registration.html',{'form':fm})






################################################################################################################################################################


# THis is dynamic url Example   


def show_details(request,my_id):
    return render (request,'dynamicurl.html')




def show_details1(request,my_id):
    if my_id==1:
        student={'id':my_id,'name':'swet'}
    if my_id==2:
        student={'id':my_id,'name':'Ashish'}
    if my_id==3:
        student={'id':my_id,'name':'Khushi'}
    
    return render (request,'dynamicurl.html',student)





# This is modelinheritance concept
from . forms import Student
from . forms import Teacher
# from . models import Modelinherit 
def student(request):
    if request.method=='POST':
        fm=Student(request.POST)
        if fm.is_valid():
           fm.save()

    else:
        fm=Student()
    return render(request,'registration.html',{'form':fm})

def teacher(request):
    if request.method=='POST':
        fm=Teacher(request.POST)
        if fm.is_valid():
           fm.save()

    else:
        fm=Teacher()
    return render(request,'registration.html',{'form':fm})












##############################################################################################################################################################


# This is messages frame work code  

from . forms import Name
from django.contrib import messages
def message(request):
    if request.method=='POST':
        fm=Name(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request,messages.SUCCESS,'Your Account is Created Successfully !!!')
            messages.info(request,'Now you can login')
            print(messages.get_level(request))
            messages.set_level(request,messages.DEBUG)
            messages.debug(request,"this is Debug")
    else:
        fm=Name()
    return render(request,'message.html/',{'form':fm})





##########################################################################################################################################################################

