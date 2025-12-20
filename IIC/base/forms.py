from django.forms import ModelForm
from django import forms
from .models import posts ,achievement , contactOrg , organisation, querys , meeting , gallery , activity , notice ,iicInfo, teamMember, certificate, ipr, incubation
from django.contrib.auth.models import User
import datetime


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

class activityFrom(ModelForm):
    class Meta:
        model = activity
        fields = "__all__"
        exclude = ["photo"]
        widgets = {
                'date': forms.DateInput(attrs={
                'type' : 'date',
                'max': datetime.date.today().strftime('%Y-%m-%d'),
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD',
                'style': 'resize: none; border-radius: 10px;'
            }), 
            'time': forms.TimeInput(attrs={
                'type' : 'time',
                'class': 'form-control',
                'placeholder': 'HH:MM',
                
                'style': 'resize: none; border-radius: 10px;'
            }), 
        }
    def clean_photo(self):
            photo = self.cleaned_data.get('photo')
            if photo:
                max_size = 2 * 1024 * 1024  # 2MB
                if photo.size > max_size:
                    raise forms.ValidationError("Image file size must be under 2MB")
            return photo

    def clean_photo(self):
            photo = self.cleaned_data.get('photo')
            if photo:
                max_size = 2 * 1024 * 1024  # 2MB
                if photo.size > max_size:
                    raise forms.ValidationError("Image file size must be under 2MB")
            return photo


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
            'date': forms.DateInput(attrs={
                'type' : 'date',
                'max': datetime.date.today().strftime('%Y-%m-%d'),
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD',
                'style': 'resize: none; border-radius: 10px;'
            }), 
            'time': forms.TimeInput(attrs={
                'type' : 'time',
                'class': 'form-control',
                'placeholder': 'HH:MM',
                
                'style': 'resize: none; border-radius: 10px;'
            }),            
        }
        exclude = ["stat"]

class iicInfoForm(ModelForm):
    class Meta:
        model = iicInfo
        fields = "__all__"

class meetingForm(ModelForm):
    class Meta:
        model = meeting
        fields = "__all__"
        widgets = {
                'date': forms.DateInput(attrs={
                'type' : 'date',
                'min': datetime.date.today().strftime('%Y-%m-%d'),
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD',
                'style': 'resize: none; border-radius: 10px;'
            }), 
            'time': forms.TimeInput(attrs={
                'type' : 'time',
                'class': 'form-control',
                'placeholder': 'HH:MM',
                
                'style': 'resize: none; border-radius: 10px;'
            }), 
        }

class galleryForm(ModelForm):
    class Meta:
        model = gallery
        fields = "__all__"
    def clean_photo(self):
            photo = self.cleaned_data.get('photo')
            if photo:
                max_size = 2 * 1024 * 1024  # 2MB
                if photo.size > max_size:
                    raise forms.ValidationError("Image file size must be under 2MB")
            return photo


class noticeForm(ModelForm):
    class Meta:
        model = notice
        fields = "__all__"
    def clean_photo(self):
            photo = self.cleaned_data.get('photo')
            if photo:
                max_size = 2 * 1024 * 1024  # 2MB
                if photo.size > max_size:
                    raise forms.ValidationError("Image file size must be under 2MB")
            return photo


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

class queryForm(ModelForm):
    class Meta:
        model = querys
        fields = "__all__"

class teamMembersForm(ModelForm):
    class Meta:
        model = teamMember
        fields = "__all__"
        exclude = ["support"]
    def clean_photo(self):
            photo = self.cleaned_data.get('photo')
            if photo:
                max_size = 2 * 1024 * 1024  # 2MB
                if photo.size > max_size:
                    raise forms.ValidationError("Image file size must be under 2MB")
            return photo

class certificateForm(ModelForm):
    class Meta:
        model = certificate
        fields = "__all__"
        
class iprForm(ModelForm):
    class Meta:
        model = ipr
        fields = "__all__"
        
class incubationForm(ModelForm):
    class Meta:
        model = incubation
        fields = "__all__"