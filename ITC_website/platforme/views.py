from django.shortcuts import render
from django.urls import is_valid_path
from .forms import  MemberForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from .models import ITC_Member
#def index(request):
  #  return render(request,'index.html')
#class LandingpageView(ListView):
      #model= homePage
     # template_name='index.html'


def home(request):
    submitted=False
    if request.method =="POST":
      form=MemberForm(request.POST)
      if form.is_valid():
          form.save()
          HttpResponseRedirect('home?submitted=true')
    else:
          form=MemberForm
          if 'submitted'in request.GET:
             submitted=True  
    
    members=ITC_Member.objects.all()

    return render(request,'index.html',{'form':form,'submitted':submitted,'members':members})


def admin(request):
    return render(request,'admin.html')
