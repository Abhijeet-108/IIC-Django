from django.shortcuts import render , redirect
from .models import dept , facult , suff , patent , copyright , conference , book , bookChapter , journal , basicDetails
from .forms import basicDetailsForm , patentForm
from django.shortcuts import render, redirect
from django.conf import settings
from .models import dept , facult , suff , patent , copyright , conference , book , bookChapter , journal
from .forms import bookForm, bookChapterForm, deptForm, facultForm, suffForm, copyrightForm, conferenceForm, journalForm
from base.models import iicInfo, querys
from django.db.models import Q
from django.http import HttpResponse
from django.template.loader import render_to_string

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def rnd(req):
    dep = dept.objects.all()
    info = iicInfo.objects.first()
    context = {"dept" : dep, 'iic' : info}
    return render(req,'rd.html', context)

def depart(req , pk):
    dep = dept.objects.get(id = pk)
    faculty = facult.objects.filter(dept = dep)
    suf = suff.objects.all()
    info = iicInfo.objects.first()
    context = {"faculty" : faculty , "suf" : suf, 'iic' : info}
    return render(req , 'depart.html' , context)

def facul(req , pk):
    faculty = facult.objects.get(id = pk)
    basic = basicDetails.objects.filter(faculty = faculty).first()
    pat = patent.objects.filter(faculty = faculty)
    copyr = copyright.objects.filter(faculty = faculty)
    books = book.objects.filter(faculty = faculty)
    bookchapters = bookChapter.objects.filter(faculty = faculty)
    journals = journal.objects.filter(faculty = faculty)
    conferences = conference.objects.filter(faculty = faculty)
    info = iicInfo.objects.first()
    context = {"faculty" : faculty , "patent" : pat , "books" : books , "journals" : journals , "bookchapters" : bookchapters , "copyrights" : copyr , "conferences" : conferences, 'iic' : info , "basicDetail" : basic}
    return render(req , 'fac.html' , context)

def basicCreate(req):
    basicsf = basicDetailsForm()
    if(req.method == "POST"):
        basicsf = basicDetails(req.POST)
        if(basicsf.is_valid()):
            basicsf.save()
        return redirect("admin-site")
    context = {'basicsf' : basicsf}
    return render(req , "form.html" , context)

def basicEdit(req , pk):
    basic = basicDetails.objects.get(id = pk)
    basicf = basicDetailsForm(instance = basic)
    if(req.method == "POST"):
        basicf = basicDetailsForm(req.POST , instance = basic)

        if basicf.is_valid():
            basicf.save()
            return redirect('admin-site')
    context = {'basicf' : basicf}
    return render(req,"form.html",context)

def basicDeletion(req , pk):
    basic = basicDetails.objects.get(id = pk)
    basic.delete()
    return redirect('admin-site')

#------------------- patent----------------------
def add_form(req):
    form = patentForm()
    if not req.user.is_superuser:
        fac = facult.objects.get(user = req.user)
    info = iicInfo.objects.first()
    if req.method == 'POST':
        form = patentForm(req.POST)
        if form.is_valid():
            if req.user.is_superuser:
                form.save()
            else:
                instance = form.save(commit = False)
                instance.faculty = fac
                instance.save()
            return redirect('research')
    else:
        form = patentForm()
    
    return render(req, 'form.html', {'form': form, 'iic' : info})

def update_form(req, pk):
    form = patent.objects.get(id = pk)
    update_form = patentForm(instance=form)
    info = iicInfo.objects.first()
    if req.method == 'POST':
        update_form = patentForm(req.POST, instance=form)
        if update_form.is_valid():
            update_form.save()
            return redirect('research')
        else:
            update_form = patentForm()
    
    return render(req, 'form.html', {'form': update_form, 'iic' : info})
    
def delete_form(req, pk):
    form = patent.objects.get(id = pk)
    form.delete()
    return redirect('research')

# -----------------dept--------------------------
def add_deptform(req):
    deptform = deptForm()
    info = iicInfo.objects.first()
    if req.method == 'POST':
        deptform = deptForm(req.POST)
        if deptform.is_valid():
            deptform.save()
            return redirect('research')
    else:
        deptform = deptForm()
    
    return render(req, 'form.html', {'form': deptform, 'iic' : info})

def update_deptform(req, pk):
    deptform = dept.objects.get(id = pk)
    info = iicInfo.objects.first()
    update_deptform = deptForm(instance=deptform)
    if req.method == 'POST':
        update_deptform = deptForm(req.POST, instance=deptform)
        if update_deptform.is_valid():
            update_deptform.save()
            return redirect('research')
        else:
            update_deptform = deptForm()
    
    return render(req, 'form.html', {'form': update_deptform, 'iic' : info})
    
def delete_deptform(req, pk):
    deptform = dept.objects.get(id = pk)
    deptform.delete()
    return redirect('research')

# ----------------bookForm------------------------
def add_bookform(req):
    bookform = bookForm()
    if not req.user.is_superuser:
        fac = facult.objects.get(user = req.user)
    info = iicInfo.objects.first()
    if req.method == 'POST':
        bookform = bookForm(req.POST)
        if bookform.is_valid():
            if req.user.is_superuser:
                bookform.save()
            else:
                instance = bookform.save(commit = False)
                instance.faculty = fac
                instance.save()
            return redirect('research')
    else:
        bookform = bookForm()
    
    return render(req, 'form.html', {'form': bookform, 'iic' : info})

def update_bookform(req, pk):
    bookform = book.objects.get(id = pk)
    update_bookform = deptForm(instance=bookform)
    info = iicInfo.objects.first()
    if req.method == 'POST':
        update_bookform = deptForm(req.POST, instance=bookform)
        if update_bookform.is_valid():
            update_bookform.save()
            return redirect('research')
        else:
            update_bookform = deptForm()
    
    return render(req, 'form.html', {'form': update_bookform, 'iic' : info})
    
def delete_bookform(req, pk):
    bookform = book.objects.get(id = pk)
    bookform.delete()
    return redirect('research')

# ---------------- Book Chapter ----------------
def add_bookChapterform(req):
    bookchapterform = bookChapterForm()
    if not req.user.is_superuser:
        fac = facult.objects.get(user = req.user)
    info = iicInfo.objects.first()
    if req.method == 'POST':
        bookchapterform = bookChapterForm(req.POST)
        if bookchapterform.is_valid():
            if req.user.is_superuser:
                bookchapterform.save()
            else:
                instance = bookchapterform.save(commit = False)
                instance.faculty = fac
                instance.save()
            return redirect('research')
    else:
        bookchapterform = bookChapterForm()
    
    return render(req, 'form.html', {'form': bookchapterform, 'iic' : info})

def update_bookChapterform(req, pk):
    bookchapterform = bookChapter.objects.get(id = pk)
    info = iicInfo.objects.first()
    update_bookchapterform = bookChapterForm(instance=bookchapterform)
    if req.method == 'POST':
        update_bookchapterform = bookChapterForm(req.POST, instance=bookchapterform)
        if update_bookchapterform.is_valid():
            update_bookchapterform.save()
            return redirect('research')
        else:
            update_bookchapterform = bookChapterForm()
    
    return render(req, 'form.html', {'form': update_bookchapterform, 'iic' : info})
    
def delete_bookChapterform(req, pk):
    bookchapterform = bookChapter.objects.get(id = pk)
    bookchapterform.delete()
    return redirect('research')


# ---------------- Faculty ----------------
def add_facultform(req):
    facultform = facultForm()
    info = iicInfo.objects.first()
    if req.method == 'POST':
        facultform = facultForm(req.POST)
        if facultform.is_valid():
            facultform.save()
            return redirect('research')
    else:
        facultform = facultForm()
    
    return render(req, 'form.html', {'form': facultform, 'iic' : info})

def update_facultform(req, pk):
    facultform = facult.objects.get(id = pk)
    info = iicInfo.objects.first()
    update_facultform = facultForm(instance=facultform)
    if req.method == 'POST':
        update_facultform = facultForm(req.POST, instance=facultform)
        if update_facultform.is_valid():
            update_facultform.save()
            return redirect('research')
        else:
            update_facultform = facultForm()
    
    return render(req, 'form.html', {'form': update_facultform, 'iic' : info})
    
def delete_facultform(req, pk):
    facultform = facult.objects.get(id = pk)
    facultform.delete()
    return redirect('research')


# ---------------- Suff ----------------
def add_suffform(req):
    suffform = suffForm()
    info = iicInfo.objects.first()
    if req.method == 'POST':
        suffform = suffForm(req.POST)
        if suffform.is_valid():
            suffform.save()
            return redirect('research')
    else:
        suffform = suffForm()
    
    return render(req, 'form.html', {'form': suffform, 'iic' : info})

def update_suffform(req, pk):
    suffform = suff.objects.get(id = pk)
    update_suffform = suffForm(instance=suffform)
    info = iicInfo.objects.first()
    if req.method == 'POST':
        update_suffform = suffForm(req.POST, instance=suffform)
        if update_suffform.is_valid():
            update_suffform.save()
            return redirect('research')
        else:
            update_suffform = suffForm()
    
    return render(req, 'form.html', {'form': update_suffform, 'iic' : info})
    
def delete_suffform(req, pk):
    suffform = suff.objects.get(id = pk)
    suffform.delete()
    return redirect('research')


# ---------------- Copyright ----------------
def add_copyrightform(req):
    copyrightform = copyrightForm()
    if not req.user.is_superuser:
        fac = facult.objects.get(user = req.user)
    info = iicInfo.objects.first()
    if req.method == 'POST':
        copyrightform = copyrightForm(req.POST)
        if copyrightform.is_valid():
            if req.user.is_superuser:
                copyrightform.save()
            else:
                instance = copyrightform.save(commit = False)
                instance.faculty = fac
                instance.save()
            return redirect('research')
    else:
        copyrightform = copyrightForm()
    
    return render(req, 'form.html', {'form': copyrightform, 'iic' : info})

def update_copyrightform(req, pk):
    copyrightform = copyright.objects.get(id = pk)
    info = iicInfo.objects.first()
    update_copyrightform = copyrightForm(instance=copyrightform)
    if req.method == 'POST':
        update_copyrightform = copyrightForm(req.POST, instance=copyrightform)
        if update_copyrightform.is_valid():
            update_copyrightform.save()
            return redirect('research')
        else:
            update_copyrightform = copyrightForm()
    
    return render(req, 'form.html', {'form': update_copyrightform, 'iic' : info})
    
def delete_copyrightform(req, pk):
    copyrightform = copyright.objects.get(id = pk)
    copyrightform.delete()
    return redirect('research')


# ---------------- Conference ----------------
def add_conferenceform(req):
    conferenceform = conferenceForm()
    if not req.user.is_superuser:
        fac = facult.objects.get(user = req.user)
    info = iicInfo.objects.first()
    if req.method == 'POST':
        conferenceform = conferenceForm(req.POST)
        if conferenceform.is_valid():
            if req.user.is_superuser:
                conferenceform.save()
            else:
                instance = conferenceform.save(commit = False)
                instance.faculty = fac
                instance.save()
            return redirect('research')
    else:
        conferenceform = conferenceForm()
    
    return render(req, 'form.html', {'form': conferenceform, 'iic' : info})

def update_conferenceform(req, pk):
    conferenceform = conference.objects.get(id = pk)
    info = iicInfo.objects.first()
    update_conferenceform = conferenceForm(instance=conferenceform)
    if req.method == 'POST':
        update_conferenceform = conferenceForm(req.POST, instance=conferenceform)
        if update_conferenceform.is_valid():
            update_conferenceform.save()
            return redirect('research')
        else:
            update_conferenceform = conferenceForm()
    
    return render(req, 'form.html', {'form': update_conferenceform, 'iic' : info})
    
def delete_conferenceform(req, pk):
    conferenceform = conference.objects.get(id = pk)
    conferenceform.delete()
    return redirect('research')


# ---------------- Journal ----------------
def add_journalform(req):
    journalform = journalForm()
    if not req.user.is_superuser:
        fac = facult.objects.get(user = req.user)
    info = iicInfo.objects.first()
    if req.method == 'POST':
        journalform = journalForm(req.POST)
        if journalform.is_valid():
            if req.user.is_superuser:
                journalform.save()
            else:
                instance = journalform.save(commit = False)
                instance.faculty = fac
                instance.save()
            return redirect('research')
    else:
        journalform = journalForm()
    
    return render(req, 'form.html', {'form': journalform, 'iic' : info})

def update_journalform(req, pk):
    journalform = journal.objects.get(id = pk)
    info = iicInfo.objects.first()
    update_journalform = journalForm(instance=journalform)
    if req.method == 'POST':
        update_journalform = journalForm(req.POST, instance=journalform)
        if update_journalform.is_valid():
            update_journalform.save()
            return redirect('research')
        else:
            update_journalform = journalForm()
    
    return render(req, 'form.html', {'form': update_journalform, 'iic' : info})
    
def delete_journalform(req, pk):
    journalform = journal.objects.get(id = pk)
    journalform.delete()
    return redirect('research')

def rndinfo(req):
    fac = facult.objects.get(user = req.user)
    basicf = basicDetailsForm()
    patentf = patentForm()
    copyrightf = copyrightForm()
    journalf = journalForm()
    bookf = bookForm()
    bookcf = bookChapterForm()
    conferencef = conferenceForm()
    if req.method == 'POST':
        basicf = basicDetailsForm(req.POST)
        patentf = patentForm(req.POST)
        copyrightf = copyrightForm(req.POST)
        journalf = journalForm(req.POST)
        bookf = bookForm(req.POST)
        bookcf = bookChapterForm(req.POST)
        conferencef = conferenceForm(req.POST)
        if basicf.is_valid():  
            instance = basicf.save(commit = False)
            instance.faculty = fac
            instance.save()
        if patentf.is_valid():
            instance = patentf.save(commit = False)
            instance.faculty = fac
            instance.save()
        if copyrightf.is_valid():
            inctsnace = copyrightf.save(commit = False)
            inctsnace.faculty = fac
            inctsnace.save()
        if journalf.is_valid():
            inctsnace = journalf.save(commit = False)
            inctsnace.faculty = fac
            inctsnace.save()
        if bookf.is_valid():
            inctsnace = bookf.save(commit = False)
            inctsnace.faculty = fac
            inctsnace.save()
        if bookcf.is_valid():
            inctsnace = bookcf.save(commit = False)
            inctsnace.faculty = fac
            inctsnace.save()
        if conferencef.is_valid():
            inctsnace = conferencef.save(commit = False)
            inctsnace.faculty = fac
            inctsnace.save()
        return redirect('home')
    else:
        basicf = basicDetailsForm()
        patentf = patentForm() 
        copyrightf = copyrightForm()
        journalf = journalForm()
        bookf = bookForm()
        bookcf = bookChapterForm()
        conferencef = conferenceForm()
   
    context = {"basicf" : basicf , "patentf" : patentf , "bookcf" : bookcf , "bookf" : bookf , "copyrightf" : copyrightf , "journalf" : journalf , "conferencef" : conferencef}
    return render(req , "rndinfo.html" , context)

def serchView(request):
    query = request.GET.get('q', '')
    result = facult.objects.none()
    info = iicInfo.objects.first()
    if query:
        result = facult.objects.filter(
            Q(name__icontains=query) |
            Q(dept__name__icontains=query) |
            Q(suf__pre__icontains=query)     
        )

    context = {'results': result, 'query': query, 'iic' : info}
    return render(request, 'search_results.html', context)

import pdfkit
pdfkit_config = pdfkit.configuration(wkhtmltopdf=settings.WKHTMLTOPDF_CMD)

def faculty_pdf(req, pk):
    
    faculty = facult.objects.get(id = pk)
    basic = basicDetails.objects.filter(faculty = faculty).first()
    pat = patent.objects.filter(faculty=faculty)
    copyr = copyright.objects.filter(faculty=faculty)
    books = book.objects.filter(faculty=faculty)
    bookchapters = bookChapter.objects.filter(faculty=faculty)
    journals = journal.objects.filter(faculty=faculty)
    conferences = conference.objects.filter(faculty=faculty)
    info = iicInfo.objects.first()
    
    photo_url = None
    if faculty.photo:
        photo_url = req.build_absolute_uri(faculty.photo.url)

    context = {
        "faculty": faculty,
        "patents": pat,
        "books": books,
        "journals": journals,
        "bookchapters": bookchapters,
        "copyrights": copyr,
        "conferences": conferences,
        "iic": info,
        "basicDetail": basic,
        "photo_url": photo_url,
    }

    html_string = render_to_string("faculty_pdf.html", context, request=req)

    options = {
        "enable-local-file-access": "",   
        "page-size": "A4",
        "encoding": "UTF-8",
        # "margin-top": "10mm",
        # "margin-right": "10mm",
        # "margin-bottom": "10mm",
        # "margin-left": "10mm",
    }
    
    pdf_content = pdfkit.from_string(html_string, False, options=options, configuration=pdfkit_config)
    
    filename = f"{faculty.name}_details.pdf".replace(" ", "_")
    response = HttpResponse(pdf_content, content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    
    return response