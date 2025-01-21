from django.shortcuts import render
from  . forms import Studentregistration
# Create your views here.
def show(request):
    fm=Studentregistration(label_suffix=' ')
    fm.order_fields(field_order=['email','name'])
    return render (request,'registration.html',{'form':fm})
