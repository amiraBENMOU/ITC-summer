
from django import forms
from django.forms import ModelForm
from .models import ITC_Member

#create a itc_members form

class MemberForm(ModelForm):
    class Meta:
        model = ITC_Member
        fields="__all__"