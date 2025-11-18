from django.shortcuts import render , redirect
from .models import posts

from django.db.models import Q

from .forms import queryForm
from .models import querys, iicInfo , notice

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def home(req):
    notices = notice.objects.all()[:10]
    post = posts.objects.all()
    queryf = queryForm()
    info = iicInfo.objects.first()
    if(req.method == "POST"):
        queryf = queryForm(req.POST)
        if(queryf.is_valid()):
            queryf.save()
        return redirect("home")
    context = {"posts" : post , 'queryf' : queryf, 'iic' : info , 'notices' : notices}
    return render(req,"a1home.html" , context)

def activities(req):
    info = iicInfo.objects.first()
    context = {'iic' : info}
    return render(req, "activity.html" , context)

def contact(req):
    info = iicInfo.objects.first()
    context = {'iic' : info}
    return render(req, "contact.html" , context)

def gallery(req):
    info = iicInfo.objects.first()
    context = {'iic' : info}
    return render(req, "gallery.html" , context)

def noticeBoard(req):
    info = iicInfo.objects.first()
    context = {'iic' : info}
    return render(req, "noticeboard.html" , context)

def achiev(req):
    info = iicInfo.objects.first()
    context = {'iic' : info}
    return render(req, "achiecvement.html" , context)

def loginFac(req):
    info = iicInfo.objects.first()
    page = 'login'
    if(req.user.is_authenticated):
        return redirect('a1home')
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
    context = {'iic' : info}
    return render(req,"a1login.html" , context)

def logoutFac(req):
    logout(req)
    return redirect('home')

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