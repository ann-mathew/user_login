from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

from .models import User 
from .forms import UserForm 

def user_welcome(request,id=id):
    instance = get_object_or_404(User,id=id)
    context ={
        "name" : instance.name,
        "instance" : instance 
    }
    return render(request,"user_welcome.html", context) 

def user_create(request):                                    
    form = UserForm(request.POST or None) 
    if form.is_valid():
        instance = form.save(commit=False)                
        instance.save() 
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {                                             
        "form": form
    }
    return render(request,"user_form.html", context)

