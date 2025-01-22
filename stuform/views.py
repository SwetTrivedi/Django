from django.shortcuts import render
from  . forms import Studentregistration
from . forms import Fields
from . forms import Back
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




def built(request):
    if request.method=='POST':
        fm=Fields(request.POST)
        if fm.is_valid():
            print('Name:',fm.cleaned_data['name'])
            print('Agree:',fm.cleaned_data['agree'])
    else:
        fm=Fields()
    return render(request,'registration.html',{'form':fm})