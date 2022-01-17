from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from .models import Candidate, Company

class CaptchaForm(forms.Form):
    captcha = CaptchaField()
# #--------------------------REGISTER FREELANCER FORM-----------------------------
# class RegisterFreelancerForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(AddNewEventForm, self).__init__(*args, **kwargs)
#         self.fields['name'].label = "Denumirea oficiala a evenimentului"
#         self.fields['locality'].label = "Localitatea"
#         self.fields['county'].label = "Judetul"
#         self.fields['country'].label = "Tara"
#         self.fields['thumbnail'].label = "O imagine daca ai"
#         self.fields['date'].label = "Introdu data"
#         self.fields['name'].widget.attrs['style'] = "width:500px"
#         self.fields['locality'].widget.attrs['style'] = "width:500px"
#         self.fields['county'].widget.attrs['style'] = "width:500px"
#         self.fields['country'].widget.attrs['style'] = "width:500px"
#     class Meta:
#         model=Candidate
#         fields=['user', 'first_name', 'last_name', 'phone', 'image', 'birthdate']
#
#         widgets = {
#             'date': DateInput(),
#             'name': forms.TextInput(attrs = {'class': 'form-control'}),
#             'locality': forms.TextInput(attrs = {'class': 'form-control'}),
#             'county': forms.TextInput(attrs = {'class': 'form-control'}),
#             'country': forms.TextInput(attrs = {'class': 'form-control'}),
#         }
# #--------------------------REGISTER FREELANCER FORM-----------------------------
# class RegisterCompanyForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(AddNewEventForm, self).__init__(*args, **kwargs)
#         self.fields['name'].label = "Denumirea oficiala a evenimentului"
#         self.fields['locality'].label = "Localitatea"
#         self.fields['county'].label = "Judetul"
#         self.fields['country'].label = "Tara"
#         self.fields['thumbnail'].label = "O imagine daca ai"
#         self.fields['date'].label = "Introdu data"
#         self.fields['name'].widget.attrs['style'] = "width:500px"
#         self.fields['locality'].widget.attrs['style'] = "width:500px"
#         self.fields['county'].widget.attrs['style'] = "width:500px"
#         self.fields['country'].widget.attrs['style'] = "width:500px"
#     class Meta:
#         model=Company
#         fields=['name', 'thumbnail', 'locality', 'county', 'country', 'date']
#
#         widgets = {
#             'date': DateInput(),
#             'name': forms.TextInput(attrs = {'class': 'form-control'}),
#             'locality': forms.TextInput(attrs = {'class': 'form-control'}),
#             'county': forms.TextInput(attrs = {'class': 'form-control'}),
#             'country': forms.TextInput(attrs = {'class': 'form-control'}),
#         }
