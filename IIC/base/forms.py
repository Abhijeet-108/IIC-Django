from django.forms import ModelForm
from django import forms
from .models import posts ,achievement , contactOrg , organisation , event, querys
from django.contrib.auth.models import User


class postForm(ModelForm):
    class Meta:
        model = posts
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title',
                'style': 'border-radius: 10px;'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post description...',
                'rows': 4,
                'style': 'resize: none; border-radius: 10px;'
            }),
        }

class achievForm(ModelForm):
    class Meta:
        model = achievement
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter achievement title',
                'style': 'border-radius: 10px;'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter achievement description...',
                'rows': 4,
                'style': 'resize: none; border-radius: 10px;'
            }),            
        }

class contactOrgForm(ModelForm):
    class Meta:
        model = contactOrg
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name',
                'style': 'border-radius: 10px;'
            }),
            'designation': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Designation...',
                'rows': 4,
                'style': 'resize: none; border-radius: 10px;'
            }),            
            'email': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email',
                'rows': 4,
                'style': 'resize: none; border-radius: 10px;'
            }),            
            'phone': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Phone Number',
                'rows': 4,
                'style': 'resize: none; border-radius: 10px;'
            }),            
            'website': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Website Link',
                'rows': 4,
                'style': 'resize: none; border-radius: 10px;'
            }),            
        }

class organisationForm(ModelForm):
    class Meta:
        model = organisation
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name',
                'style': 'border-radius: 10px;'
            }),
            'thrustarea': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '',
                'rows': 4,
                'style': 'resize: none; border-radius: 10px;'
            }),            
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter City',
                'style': 'border-radius: 10px;'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Address',
                'style': 'border-radius: 10px;'
            }),
            'contact': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Contact',
                'style': 'border-radius: 10px;'
            }),
            'stage': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select Stage',
                'style': 'border-radius: 10px;'
            }),
            'stat': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select Status',
                'style': 'border-radius: 10px;'
            }),
        }

class eventForm(ModelForm):
    class Meta:
        model = event
        fields = "__all__"
        widgets = {
            'date': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Date',
                'style': 'border-radius: 10px;'
            }),
            'headline': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Headline',
                'rows': 4,
                'style': 'resize: none; border-radius: 10px;'
            }),            
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Description',
                'style': 'border-radius: 10px;'
            }),
            'stat': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select Status',
                'style': 'border-radius: 10px;'
            }),
            'faculty': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select Facluties',
                'style': 'border-radius: 10px;'
            }),
        }

class queryForm(ModelForm):
    class Meta:
        models = querys
        fields = "__all__"
        widgets = {
            'fullname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Full Name',
                'style': 'border-radius: 10px;'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email',
                'style': 'border-radius: 10px;'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Phone Number',
                'style': 'border-radius: 10px;'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Select Subject',
                'style': 'border-radius: 10px;'
            }),            
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Type you Query Here ... ',
                'rows': 4,
                'style': 'resize: none; border-radius: 10px;'
            }),
    }