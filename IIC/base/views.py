from django.shortcuts import render , redirect
from .models import posts

from django.db.models import Q

from .forms import queryForm , teamMembersForm, certificateForm, iprForm , incubationForm , activityFrom
from rnd.forms import facultForm
from .models import querys, iicInfo , notice , meeting , achievement , gallery , activity, teamMember , certificate , ipr , incubation

from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.utils import timezone


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
    current_year = timezone.now().year
    previous_year = timezone.now().year - 1
    info = iicInfo.objects.first()
    calact = activity.objects.filter(category = "IIC Calender Activity")
    micact = activity.objects.filter(category = "MIC Driven Activity")
    celebact = activity.objects.filter(category = "Celebration Activity")
    selfact = activity.objects.filter(category = "Self Driven Activity")
    previous = activity.objects.filter(date__year = previous_year)
    current = activity.objects.filter(date__year = current_year)

    context = {'iic' : info , 'calact' : calact , 'micact' : micact , 'celebact' : celebact , 'selfact' : selfact  , 'previous' : previous , 'current' : current}
    return render(req, "acti.html" , context)

def meet(req):
    meetings = meeting.objects.all()[:20]
    info = iicInfo.objects.first()
    context = {'iic' : info , "meetings" : meetings}
    return render(req, "meetingdisplay.html" , context)

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
        form1 = facultForm(req.POST , req.FILES)
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

def queryDeletion(req, pk):
    query = querys.objects.get(id = pk)
    query.delete()
    return redirect('admin-profile')

#-------------------------- Team Members Page ----------------------- #
def teamMenbers(req):
    teamMembers = teamMember.objects.all()
    info = iicInfo.objects.first()
    administrative = teamMember.objects.filter(Q(role="Convenor") | Q(role="Co-Convenor") | Q(role="Convenor of External Affairs") | Q(role="Hult Prize Campus Director & Operations Head") | Q(role="Chief Financial & Strategic Advisor"))
    heads_cohead = teamMember.objects.filter(Q(role="Head of Tech Wing") | Q(role="Co-Head of Tech Wing")|Q(role="Head of Graphics Wing") | Q(role="Co-Head of Graphics Wing")|Q(role="Head of Startup Wing") | Q(role="Co-Head of Startup Wing")|Q(role="Head of Public Relations And Outreach wing") | Q(role="Co-Head of Public Relations And Outreach wing")|Q(role="Head of Management and Resource wing") | Q(role="Co-Head of Management and Resource wing")|Q(role="Head of Social Media Wing") | Q(role="Co-Head of Social Media Wing")|Q(role="Head of Sponsorship Wing") | Q(role="Co-Head of Sponsorship Wing")|Q(role="Head of Content Wing") | Q(role="Co-Head of Content Wing"))
    context = {'iic' : info , 'teamMembers' : teamMembers, 'administrative' : administrative , 'heads_cohead' : heads_cohead}
    return render(req, "teamForm.html" , context)



def addteamMembers(req):
    page = 'Add Team Members'
    addteamMembersf = teamMembersForm()
    info = iicInfo.objects.first()
    if(req.method == "POST"):
        addteamMembersf = teamMembersForm(req.POST, req.FILES)
        if(addteamMembersf.is_valid()):
            addteamMembersf.save()
        return redirect("team_members")
    
    return render(req , "Form3.html" , {'Form' : addteamMembersf, 'page' : page, 'iic' : info})

def updateteamMembers(req , pk):
    page = 'Update Team Members'
    teammember = teamMember.objects.get(id = pk)
    updateteamMembersf = teamMembersForm(instance = teammember)
    if(req.method == "POST"):
        updateteamMembersf = teamMembersForm(req.POST , instance = teammember)
        if(updateteamMembersf.is_valid()):
            updateteamMembersf.save()
            return redirect("admin-site")
        else:
            updateteamMembersf = teamMembersForm()
    
    return render(req , "Form3.html" , {'Form' : updateteamMembersf, 'page' : page})

def deleteteamMembers(req, pk):
    teammember = teamMember.objects.get(id = pk)
    teammember.delete()
    return redirect('team_members')

# --------------------------Certificate------------------------------ #

def certificates(req):
    cert = certificate.objects.all()
    info = iicInfo.objects.first()
    context = {'iic' : info , 'certificates' : cert}
    return render(req, "certificate.html" , context)

def addcertificate(req):
    page = 'Add Certificate'
    certificatef = certificateForm()
    info = iicInfo.objects.first()
    if(req.method == "POST"):
        certificatef = certificateForm(req.POST , req.FILES)
        if(certificatef.is_valid()):
            certificatef.save()
        return redirect("certificate")
    
    return render(req , "Form3.html" , {'Form' : certificatef, 'page' : page, 'iic' : info})

def updatecertificate(req , pk):
    page = 'Update Certificate'
    certificatee = certificate.objects.get(id = pk)
    updatecertificatef = certificateForm(instance = certificatee)
    if(req.method == "POST"):
        updatecertificatef = certificateForm(req.POST , req.FILES , instance = certificatee)
        if(updatecertificatef.is_valid()):
            updatecertificatef.save()
            return redirect("admin-site")
        else:
            updatecertificatef = certificateForm()
    
    return render(req , "Form3.html" , {'Form' : updatecertificatef, 'page' : page})

def deletecertificate(req, pk):
    certificatee = certificate.objects.get(id = pk)
    certificatee.delete()
    return redirect('certificate')

# -------------------------- IPR ------------------------------ #

def iprs(req):
    iprs = ipr.objects.all()
    info = iicInfo.objects.first()
    context = {'iic' : info , 'iprs' : iprs}
    return render(req, "ipr.html" , context)

def addipr(req):
    page = 'Add IPR'
    iprf = iprForm()
    info = iicInfo.objects.first()
    if(req.method == "POST"):
        iprf = iprForm(req.POST , req.FILES)
        if(iprf.is_valid()):
            iprf.save()
        return redirect("ipr")
    
    return render(req , "Form3.html" , {'Form' : iprf, 'page' : page, 'iic' : info})

def updateipr(req , pk):
    page = 'Update IPR'
    ipre = ipr.objects.get(id = pk)
    updateiprf = iprForm(instance = ipre)
    if(req.method == "POST"):
        updateiprf = iprForm(req.POST , req.FILES , instance = ipre)
        if(updateiprf.is_valid()):
            updateiprf.save()
            return redirect("ipr")
        else:
            updateiprf = iprForm()
    
    return render(req , "form2.html" , {'form' : updateiprf, 'page' : page})

def deleteipr(req, pk):
    ipre = ipr.objects.get(id = pk)
    ipre.delete()
    return redirect('ipr')

# -------------------------- Incubation ------------------------------ #

def incubations(req):
    incubations = incubation.objects.all()
    info = iicInfo.objects.first()
    context = {'iic' : info , 'incubations' : incubations}
    return render(req, "incubator.html" , context)

def addincubation(req):
    page = 'Add Incubation'
    incubationf = incubationForm()
    info = iicInfo.objects.first()
    if(req.method == "POST"):
        incubationf = incubationForm(req.POST , req.FILES)
        if(incubationf.is_valid()):
            incubationf.save()
        return redirect("admin-site")
    
    return render(req , "Form3.html" , {'Form' : incubationf, 'page' : page, 'iic' : info})

def updateincubation(req , pk):
    page = 'Update Incubation'
    incubatione = incubation.objects.get(id = pk)
    updateincubationf = incubationForm(instance = incubatione)
    if(req.method == "POST"):
        updateincubationf = incubationForm(req.POST , req.FILES , instance = incubatione)
        if(updateincubationf.is_valid()):
            updateincubationf.save()
            return redirect("admin-site")
        else:
            updateincubationf = incubationForm()
    
    return render(req , "Form3.html" , {'Form' : updateincubationf, 'page' : page})

def deleteincubation(req, pk):
    incubatione = incubation.objects.get(id = pk)
    incubatione.delete()
    return redirect('admin-site')


# ------------------------------ Activity -----------------------------

def addactivity(req):
    page = 'Add Activity'
    actf = activityFrom()
    if(req.method == "POST"):
        actf = activityFrom(req.POST , req.FILES)
        if(actf.is_valid()):
            actf.save()
        return redirect("activities")
    
    return render(req , "actform.html" , {'form' : actf, 'page' : page})

def updateactivity(req , pk):
    page = 'Update Activity'
    act = activity.objects.get(id = pk)
    actf = activityFrom(instance = act)
    if(req.method == "POST"):
        actf = activityFrom(req.POST , req.FILES , instance = act)
        if(actf.is_valid()):
            actf.save()
            return redirect("activities")
        else:
            actf = activityFrom()
    
    return render(req , "actform.html" , {'form' : actf, 'page' : page})

def deleteactivity(req , pk):
    print(pk)
    act = activity.objects.get(id = pk)
    act.delete()
    return redirect('activities')