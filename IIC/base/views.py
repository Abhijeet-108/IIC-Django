from django.shortcuts import render , redirect
from .models import posts

from django.db.models import Q

from .forms import queryForm 
from rnd.forms import facultForm
from .models import querys, iicInfo , notice , meeting , achievement , gallery , activity

from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




# Create your views here.

def home(req):
    notices = notice.objects.all()[:6]
    meets = meeting.objects.all()[:6]
    post = posts.objects.all()
    queryf = queryForm()
    info = iicInfo.objects.first()
    if(req.method == "POST"):
        queryf = queryForm(req.POST)
        if(queryf.is_valid()):
            queryf.save()
        return redirect("home")
    context = {"posts" : post , 'queryf' : queryf, 'iic' : info , 'notices' : notices , 'meets' : meets}
    return render(req,"a1home.html" , context)

def activities(req):
    info = iicInfo.objects.first()
    context = {'iic' : info}
    return render(req, "activity.html" , context)

def meet(req):
    meetings = meeting.objects.all()[:20]
    info = iicInfo.objects.first()
    context = {'iic' : info , "meetings" : meetings}
    return render(req, "meethome.html" , context)

def contact(req):
    info = iicInfo.objects.first()
    context = {'iic' : info}
    return render(req, "contact.html" , context)

def galleryPage(req):
    images = gallery.objects.all()
    info = iicInfo.objects.first()
    context = {'iic' : info , 'images' : images}
    return render(req, "gallery.html" , context)

def noticeBoard(req):
    notices = notice.objects.all()[:20]
    info = iicInfo.objects.first()
    context = {'iic' : info , 'notices' : notices}
    return render(req, "noticeboard.html" , context)

def achiev(req):
    ach = achievement.objects.all()[:50]
    info = iicInfo.objects.first()
    context = {'iic' : info , 'ach' : ach}
    return render(req, "achievement.html" , context)

# --------------------------login & register ----------------------- #

def registerFac(req):
    info = iicInfo.objects.first()
    page = 'register'
    form = UserCreationForm()
    form1 = facultForm()
    if(req.method == "POST"):
        count = 0
        form = UserCreationForm(req.POST)
        form1 = facultForm(req.POST)
        if(form.is_valid):
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            login(req , user)
            count += 1
        if(form1.is_valid):
            fac = form1.save(commit = False)
            fac.user = req.user
            fac.save()
            count +=1
        if(count == 2):
            return redirect('rndinfo')
    context = {'iic' : info , 'page' : page , 'form' : form , 'form1' : form1}
    return render(req , 'signup1.html' , context)

def loginFac(req):
    info = iicInfo.objects.first()
    page = 'login'
    if(req.user.is_authenticated):
        if(req.user.is_superuser):
            return redirect('admin-site')
        return redirect('home')
    if(req.method == "POST"):
        username = req.POST.get('username')
        password = req.POST.get('password')
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(req , 'User does not exist!')
        user1 = authenticate(req , username = username , password = password)
        if user1 is not None:
            login(req , user1)
            if user1.is_superuser:
                return redirect('admin-site')
            else:
                return redirect('home')
        else:
            messages.error(req, 'Username or Password is not correct!')
    context = {'iic' : info , 'page' : page}
    return render(req,"a1login.html" , context)

def logoutFac(req):
    logout(req)
    return redirect('home')

# ------------------------------------------------------------------------ #

def queryCreate(req):
    queryf = queryForm()
    if(req.method == "POST"):
        queryf = queryForm(req.POST)
        if(queryf.is_valid()):
            queryf.save()
        return redirect("admin-site")
    context = {'queryf' : queryf}
    return render(req , "form2.html" , context)

def queryDeletion(req , pk):
    query = querys.objects.get(id = pk)
    query.delete()
    return redirect('admin-site')

