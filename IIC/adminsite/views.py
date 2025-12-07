from django.shortcuts import render , redirect
from base.models import posts , achievement, organisation , contactOrg , notice , meeting , gallery , iicInfo
from base.forms import postForm , achievForm , contactOrgForm , organisationForm , meetingForm , galleryForm , noticeForm , iicInfoForm , querys
from django.contrib.auth.models import User
from base.models import iicInfo
from rnd.models import facult
# Create your views here.

def homepage(req):
    notices = notice.objects.all()[:6]
    meets = meeting.objects.all()[:6]
    info = iicInfo.objects.first()
    if not req.user.is_superuser:
        return redirect('home')
    post = posts.objects.all()
    context = {"posts" : post, 'iic' : info , 'notices' : notices , 'meets' : meets}
    return render(req , 'adminhome.html' , context)

def profilePage(req):
    info = iicInfo.objects.first()
    context = {'iic' : info}
    if (not req.user.is_superuser):
        fac = facult.objects.get(user = req.user)
        meet = meeting.objects.filter(faculty = fac)
        context['fac'] = fac
        context['meet'] = meet
    else:
        query = querys.objects.all()
        context['query'] = query
    return render(req , 'adminprofile.html' , context)

def postCreate(req):
    postf = postForm()
    info = iicInfo.objects.first()
    if(req.method == "POST"):
        postf = postForm(req.POST)
        if(postf.is_valid()):
            postf.save()
        return redirect("admin-site")
    context = {'postf' : postf, 'iic' : info}
    return render(req , "form1.html" , context)

def postEdit(req , pk):
    post = posts.objects.get(id = pk)
    postf = postForm(instance = post)
    info = iicInfo.objects.first()
    if(req.method == "POST"):
        postf = postForm(req.POST , instance = post)

        if postf.is_valid():
            postf.save()
            return redirect('admin-site')
    context = {'postf' : postf, 'iic' : info}
    return render(req,"form1.html",context)

def postDeletion(req , pk):
    post = posts.objects.get(id = pk)
    post.delete()
    return redirect('admin-site')

def achievCreate(req):
    achievf = achievForm()
    if(req.method == "POST"):
        achievf = achievForm(req.POST , req.FILES)
        if(achievf.is_valid()):
            achievf.save()
        return redirect("admin-site")
    context = {'achievf' : achievf}
    return render(req , "form1.html" , context)

def achievEdit(req , pk):
    achiev = achievement.objects.get(id = pk)
    achievf = achievForm(instance = achiev)
    if(req.method == "POST"):
        achievf = achievForm(req.POST , req.FILES , instance = achiev)

        if achievf.is_valid():
            achievf.save()
            return redirect('admin-site')
    context = {'achievf' : achievf}
    return render(req,"form1.html",context)

def achievDeletion(req , pk):
    achiev = achievement.objects.get(id = pk)
    achiev.delete()
    return redirect('admin-site')

def contactOrgCreate(req):
    contactf = contactOrgForm()
    if(req.method == "POST"):
        contactf = contactOrgForm(req.POST)
        if(contactf.is_valid()):
            contactf.save()
        return redirect("admin-site")
    context = {'contactf' : contactf}
    return render(req , "form1.html" , context)

def contactOrgEdit(req , pk):
    contact = contactOrg.objects.get(id = pk)
    contactf = contactOrgForm(instance = contact)
    if(req.method == "POST"):
        contactf = contactOrgForm(req.POST , instance = contact)

        if contactf.is_valid():
            contactf.save()
            return redirect('admin-site')
    context = {'contactf' : contactf}
    return render(req,"form1.html",context)

def contactOrgDeletion(req , pk):
    contact = contactOrg.objects.get(id = pk)
    contact.delete()
    return redirect('admin-site')

def organisationCreate(req):
    organisationf = organisationForm()
    if(req.method == "POST"):
        organisationf = organisationForm(req.POST)
        if(organisationf.is_valid()):
            organisationf.save()
        return redirect("admin-site")
    context = {'organisationf' : organisationf}
    return render(req , "form1.html" , context)

def organisationEdit(req , pk):
    organisations = organisation.objects.get(id = pk)
    organisationf = organisationForm(instance = organisations)
    if(req.method == "POST"):
        organisationf = organisationForm(req.POST , instance = organisations)

        if organisationf.is_valid():
            organisationf.save()
            return redirect('admin-site')
    context = {'organisationf' : organisationf}
    return render(req,"form1.html",context)

def organisationDeletion(req , pk):
    organisations = organisation.objects.get(id = pk)
    organisations.delete()
    return redirect('admin-site')

# ---------------- Meeting ----------------
def add_meetform(req):
    meetform = meetingForm()
    if req.method == 'POST':
        meetform = meetingForm(req.POST)
        if meetform.is_valid():
            meetform.save()
            return redirect('meet')
    else:
        meetform = meetingForm()
    
    return render(req, 'meeting1.html', {'meetf': meetform})

def update_meetform(req, pk):
    meetform = meeting.objects.get(id = pk)
    update_meetformform = meetingForm(instance=meetform)
    if req.method == 'POST':
        update_meetformform = meetingForm(req.POST, instance=meetform)
        if update_meetformform.is_valid():
            update_meetformform.save()
            return redirect('meet')
        else:
            update_meetformform = meetingForm()
    
    return render(req, 'meeting11.html', {'meetf': update_meetformform})
    
def delete_meetform(req, pk):
    meetform = meeting.objects.get(id = pk)
    meetform.delete()
    return redirect('meet')

# ---------------- Gallery ----------------

def galleryCreate(req):
    galleryf = galleryForm()
    info = iicInfo.objects.first()
    if(req.method == "POST"):
        galleryf = galleryForm(req.POST , req.FILES)
        if(galleryf.is_valid()):
            galleryf.save()
        return redirect("gallery")
    context = {'galleryf' : galleryf, 'iic' : info}
    return render(req , "form1.html" , context)

def galleryDeletion(req , pk):
    post = gallery.objects.get(id = pk)
    post.delete()
    return redirect('gallery')

# ---------------- Notice ----------------

def noticeCreate(req):
    noticef = noticeForm()
    info = iicInfo.objects.first()
    if(req.method == "POST"):
        noticef = noticeForm(req.POST , req.FILES)
        if(noticef.is_valid()):
            noticef.save()
        return redirect("notice")
    context = {'noticef' : noticef, 'iic' : info}
    return render(req , "form1.html" , context)

def noticeEdit(req , pk):
    notices = notice.objects.get(id = pk)
    noticef = noticef(instance = notices)
    info = iicInfo.objects.first()
    if(req.method == "POST"):
        noticef = noticeForm(req.POST , req.FILES , instance = notices)

        if noticef.is_valid():
            noticef.save()
            return redirect('notice')
    context = {'noticef' : noticef, 'iic' : info}
    return render(req,"form1.html",context)

def noticeDeletion(req , pk):
    post = notice.objects.get(id = pk)
    post.delete()
    return redirect('notice')

# ---------------- IIC-Info ----------------

def iicInfoEdit(req):
    info = iicInfo.objects.first()
    iicf = iicInfoForm(instance = info)
    if(req.method == "POST"):
        iicf = iicInfoForm(req.POST , req.FILES , instance = info)

        if iicf.is_valid():
            iicf.save()
            return redirect('admin-profile')
    context = {'iicf' : iicf, 'iic' : info}
    return render(req,"form1.html",context)

