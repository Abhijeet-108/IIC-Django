from django.shortcuts import render, redirect
from .models import dept , facult , suff , patent , copyright , conference , book , bookChapter , journal
from .forms import Form, bookForm, bookChapterForm, deptForm, facultForm, suffForm, copyrightForm, conferenceForm, journalForm

# Create your views here.

def rnd(req):
    dep = dept.objects.all()
    context = {"dept" : dep}
    return render(req,'rd.html', context)

def depart(req , pk):
    dep = dept.objects.get(id = pk)
    faculty = facult.objects.filter(dept = dep)
    suf = suff.objects.all()
    context = {"faculty" : faculty , "suf" : suf}
    return render(req , 'depart.html' , context)

def facul(req , pk):
    faculty = facult.objects.get(id = pk)
    pat = patent.objects.filter(faculty = faculty)
    copyr = copyright.objects.filter(faculty = faculty)
    books = book.objects.filter(faculty = faculty)
    bookchapters = bookChapter.objects.filter(faculty = faculty)
    journals = journal.objects.filter(faculty = faculty)
    conferences = conference.objects.filter(faculty = faculty)
    context = {"faculty" : faculty , "patent" : pat , "books" : books , "journals" : journals , "bookchapters" : bookchapters , "copyrights" : copyr , "conferences" : conferences}
    return render(req , 'faculty.html' , context)


#------------------- patent----------------------
def add_form(req):
    form = Form()
    if req.method == 'POST':
        form = Form(req.POST)
        if form.is_valid():
            form.save()
            return redirect('research')
    else:
        form = Form()
    
    return render(req, 'form.html', {'form': form})

def update_form(req, pk):
    form = patent.objects.get(id = pk)
    update_form = Form(instance=form)
    if req.method == 'POST':
        update_form = Form(req.POST, instance=form)
        if update_form.is_valid():
            update_form.save()
            return redirect('research')
        else:
            update_form = Form()
    
    return render(req, 'form.html', {'form': update_form})
    
def delete_form(req, pk):
    form = patent.objects.get(id = pk)
    form.delete()
    return redirect('research')

# -----------------dept--------------------------
def add_deptform(req):
    deptform = deptForm()
    if req.method == 'POST':
        deptform = deptForm(req.POST)
        if deptform.is_valid():
            deptform.save()
            return redirect('research')
    else:
        deptform = deptForm()
    
    return render(req, 'form.html', {'form': deptform})

def update_deptform(req, pk):
    deptform = dept.objects.get(id = pk)
    update_deptform = deptForm(instance=deptform)
    if req.method == 'POST':
        update_deptform = deptForm(req.POST, instance=deptform)
        if update_deptform.is_valid():
            update_deptform.save()
            return redirect('research')
        else:
            update_deptform = deptForm()
    
    return render(req, 'form.html', {'form': update_deptform})
    
def delete_deptform(req, pk):
    deptform = dept.objects.get(id = pk)
    deptform.delete()
    return redirect('research')

# ----------------bookForm------------------------
def add_bookform(req):
    bookform = bookForm()
    if req.method == 'POST':
        bookform = bookForm(req.POST)
        if bookform.is_valid():
            bookform.save()
            return redirect('research')
    else:
        bookform = bookForm()
    
    return render(req, 'form.html', {'form': bookform})

def update_bookform(req, pk):
    bookform = book.objects.get(id = pk)
    update_bookform = deptForm(instance=bookform)
    if req.method == 'POST':
        update_bookform = deptForm(req.POST, instance=bookform)
        if update_bookform.is_valid():
            update_bookform.save()
            return redirect('research')
        else:
            update_bookform = deptForm()
    
    return render(req, 'form.html', {'form': update_bookform})
    
def delete_bookform(req, pk):
    bookform = book.objects.get(id = pk)
    bookform.delete()
    return redirect('research')

# ---------------- Book Chapter ----------------
def add_bookChapterform(req):
    bookchapterform = bookChapterForm()
    if req.method == 'POST':
        bookchapterform = bookChapterForm(req.POST)
        if bookchapterform.is_valid():
            bookchapterform.save()
            return redirect('research')
    else:
        bookchapterform = bookChapterForm()
    
    return render(req, 'form.html', {'form': bookchapterform})

def update_bookChapterform(req, pk):
    bookchapterform = bookChapter.objects.get(id = pk)
    update_bookchapterform = bookChapterForm(instance=bookchapterform)
    if req.method == 'POST':
        update_bookchapterform = bookChapterForm(req.POST, instance=bookchapterform)
        if update_bookchapterform.is_valid():
            update_bookchapterform.save()
            return redirect('research')
        else:
            update_bookchapterform = bookChapterForm()
    
    return render(req, 'form.html', {'form': update_bookchapterform})
    
def delete_bookChapterform(req, pk):
    bookchapterform = bookChapter.objects.get(id = pk)
    bookchapterform.delete()
    return redirect('research')


# ---------------- Faculty ----------------
def add_facultform(req):
    facultform = facultForm()
    if req.method == 'POST':
        facultform = facultForm(req.POST)
        if facultform.is_valid():
            facultform.save()
            return redirect('research')
    else:
        facultform = facultForm()
    
    return render(req, 'form.html', {'form': facultform})

def update_facultform(req, pk):
    facultform = facult.objects.get(id = pk)
    update_facultform = facultForm(instance=facultform)
    if req.method == 'POST':
        update_facultform = facultForm(req.POST, instance=facultform)
        if update_facultform.is_valid():
            update_facultform.save()
            return redirect('research')
        else:
            update_facultform = facultForm()
    
    return render(req, 'form.html', {'form': update_facultform})
    
def delete_facultform(req, pk):
    facultform = facult.objects.get(id = pk)
    facultform.delete()
    return redirect('research')


# ---------------- Suff ----------------
def add_suffform(req):
    suffform = suffForm()
    if req.method == 'POST':
        suffform = suffForm(req.POST)
        if suffform.is_valid():
            suffform.save()
            return redirect('research')
    else:
        suffform = suffForm()
    
    return render(req, 'form.html', {'form': suffform})

def update_suffform(req, pk):
    suffform = suff.objects.get(id = pk)
    update_suffform = suffForm(instance=suffform)
    if req.method == 'POST':
        update_suffform = suffForm(req.POST, instance=suffform)
        if update_suffform.is_valid():
            update_suffform.save()
            return redirect('research')
        else:
            update_suffform = suffForm()
    
    return render(req, 'form.html', {'form': update_suffform})
    
def delete_suffform(req, pk):
    suffform = suff.objects.get(id = pk)
    suffform.delete()
    return redirect('research')


# ---------------- Copyright ----------------
def add_copyrightform(req):
    copyrightform = copyrightForm()
    if req.method == 'POST':
        copyrightform = copyrightForm(req.POST)
        if copyrightform.is_valid():
            copyrightform.save()
            return redirect('research')
    else:
        copyrightform = copyrightForm()
    
    return render(req, 'form.html', {'form': copyrightform})

def update_copyrightform(req, pk):
    copyrightform = copyright.objects.get(id = pk)
    update_copyrightform = copyrightForm(instance=copyrightform)
    if req.method == 'POST':
        update_copyrightform = copyrightForm(req.POST, instance=copyrightform)
        if update_copyrightform.is_valid():
            update_copyrightform.save()
            return redirect('research')
        else:
            update_copyrightform = copyrightForm()
    
    return render(req, 'form.html', {'form': update_copyrightform})
    
def delete_copyrightform(req, pk):
    copyrightform = copyright.objects.get(id = pk)
    copyrightform.delete()
    return redirect('research')


# ---------------- Conference ----------------
def add_conferenceform(req):
    conferenceform = conferenceForm()
    if req.method == 'POST':
        conferenceform = conferenceForm(req.POST)
        if conferenceform.is_valid():
            conferenceform.save()
            return redirect('research')
    else:
        conferenceform = conferenceForm()
    
    return render(req, 'form.html', {'form': conferenceform})

def update_conferenceform(req, pk):
    conferenceform = conference.objects.get(id = pk)
    update_conferenceform = conferenceForm(instance=conferenceform)
    if req.method == 'POST':
        update_conferenceform = conferenceForm(req.POST, instance=conferenceform)
        if update_conferenceform.is_valid():
            update_conferenceform.save()
            return redirect('research')
        else:
            update_conferenceform = conferenceForm()
    
    return render(req, 'form.html', {'form': update_conferenceform})
    
def delete_conferenceform(req, pk):
    conferenceform = conference.objects.get(id = pk)
    conferenceform.delete()
    return redirect('research')


# ---------------- Journal ----------------
def add_journalform(req):
    journalform = journalForm()
    if req.method == 'POST':
        journalform = journalForm(req.POST)
        if journalform.is_valid():
            journalform.save()
            return redirect('research')
    else:
        journalform = journalForm()
    
    return render(req, 'form.html', {'form': journalform})

def update_journalform(req, pk):
    journalform = journal.objects.get(id = pk)
    update_journalform = journalForm(instance=journalform)
    if req.method == 'POST':
        update_journalform = journalForm(req.POST, instance=journalform)
        if update_journalform.is_valid():
            update_journalform.save()
            return redirect('research')
        else:
            update_journalform = journalForm()
    
    return render(req, 'form.html', {'form': update_journalform})
    
def delete_journalform(req, pk):
    journalform = journal.objects.get(id = pk)
    journalform.delete()
    return redirect('research')