from django import forms
from rnd.models import dept , facult , suff , patent , copyright , conference , book , bookChapter , journal

class Form(forms.ModelForm):
    class Meta:
        model = patent
        fields = "__all__"
        exculde = ['faculty']
        
class bookForm(forms.ModelForm):
    class Meta:
        model = book
        fields = "__all__"
        eexculde = ['faculty']

class deptForm(forms.ModelForm):
    class Meta:
        model = dept
        fields = "__all__"
        exculde = ['faculty']

class facultForm(forms.ModelForm):
    class Meta:
        model = facult
        fields = "__all__"
        exculde = ['faculty']

class suffForm(forms.ModelForm):
    class Meta:
        model = suff
        fields = "__all__"
        exculde = ['faculty']
        
class copyrightForm(forms.ModelForm):
    class Meta:
        model = copyright
        fields = "__all__"
        exculde = ['faculty']
        
class conferenceForm(forms.ModelForm):
    class Meta:
        model = conference
        fields = "__all__"
        exculde = ['faculty']
        
class bookChapterForm(forms.ModelForm):
    class Meta:
        model = bookChapter
        fields = "__all__"
        exculde = ['faculty']
        
class journalForm(forms.ModelForm):
    class Meta:
        model = journal
        fields = "__all__"
        exculde = ['faculty']