from django.shortcuts import render , redirect
from base.models import posts , achievement , event , organisation , contactOrg
from base.forms import postForm , achievForm , eventForm , contactOrgForm , organisationForm
from django.contrib.auth.models import User

# Create your views here.

def homepage(req):
    if not req.user.is_superuser:
        return redirect('home')
    post = posts.objects.all()
    context = {"posts" : post}
    return render(req , 'adminhome.html' , context)

def postCreate(req):
    postf = postForm()
    if(req.method == "POST"):
        postf = postForm(req.POST)
        if(postf.is_valid()):
            postf.save()
        return redirect("admin-site")
    context = {'postf' : postf}
    return render(req , "form1.html" , context)

def postEdit(req , pk):
    post = posts.objects.get(id = pk)
    postf = postForm(instance = post)
    if(req.method == "POST"):
        postf = postForm(req.POST , instance = post)

        if postf.is_valid():
            postf.save()
            return redirect('admin-site')
    context = {'postf' : postf}
    return render(req,"form1.html",context)

def postDeletion(req , pk):
    post = posts.objects.get(id = pk)
    post.delete()
    return redirect('admin-site')

def achievCreate(req):
    achievf = achievForm()
    if(req.method == "POST"):
        achievf = achievForm(req.POST)
        if(achievf.is_valid()):
            achievf.save()
        return redirect("admin-site")
    context = {'achievf' : achievf}
    return render(req , "form1.html" , context)

def achievEdit(req , pk):
    achiev = achievement.objects.get(id = pk)
    achievf = achievForm(instance = achiev)
    if(req.method == "POST"):
        achievf = achievForm(req.POST , instance = achiev)

        if achievf.is_valid():
            achievf.save()
            return redirect('admin-site')
    context = {'achievf' : achievf}
    return render(req,"form1.html",context)

def achievDeletion(req , pk):
    achiev = achievement.objects.get(id = pk)
    achiev.delete()
    return redirect('admin-site')

def eventCreate(req):
    eventf = eventForm()
    if(req.method == "POST"):
        eventf = eventForm(req.POST)
        if(eventf.is_valid()):
            eventf.save()
        return redirect("admin-site")
    context = {'eventf' : eventf}
    return render(req , "form1.html" , context)

def eventEdit(req , pk):
    events = event.objects.get(id = pk)
    eventf = eventForm(instance = events)
    if(req.method == "POST"):
        eventf = eventForm(req.POST , instance = events)

        if eventf.is_valid():
            eventf.save()
            return redirect('admin-site')
    context = {'eventf' : eventf}
    return render(req,"form1.html",context)

def eventDeletion(req , pk):
    events = event.objects.get(id = pk)
    events.delete()
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