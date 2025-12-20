from django.forms import ModelForm
from django import forms
from .models import basicDetails
from django.contrib.auth.models import User

class basicDetailsForm(ModelForm):
    class Meta:
        model = basicDetails
        fields = "__all__"
        exclude = ["faculty"]        
from django import forms
from rnd.models import dept , facult , suff , patent , copyright , conference , book , bookChapter , journal

class patentForm(forms.ModelForm):
    class Meta:
        model = patent
        fields = "__all__"
        exclude = ['faculty']
        
class bookForm(forms.ModelForm):
    class Meta:
        model = book
        fields = "__all__"
        exclude = ['faculty']

class deptForm(forms.ModelForm):
    class Meta:
        model = dept
        fields = "__all__"
        exclude = ['faculty']

class facultForm(forms.ModelForm):
    class Meta:
        model = facult
        fields = "__all__"
        exclude = ['user']

    def clean_photo(self):
            photo = self.cleaned_data.get('photo')
            if photo:
                max_size = 2 * 1024 * 1024  # 2MB
                if photo.size > max_size:
                    raise forms.ValidationError("Image file size must be under 2MB")
            return photo

class suffForm(forms.ModelForm):
    class Meta:
        model = suff
        fields = "__all__"
        exclude = ['faculty']
        
class copyrightForm(forms.ModelForm):
    class Meta:
        model = copyright
        fields = "__all__"
        exclude = ['faculty']
        
class conferenceForm(forms.ModelForm):
    class Meta:
        model = conference
        fields = "__all__"
        exclude = ['faculty']
        
class bookChapterForm(forms.ModelForm):
    class Meta:
        model = bookChapter
        fields = "__all__"
        exclude = ['faculty']
        
class journalForm(forms.ModelForm):
    class Meta:
        model = journal
        fields = "__all__"
        exclude = ['faculty']
