from django.shortcuts import render , redirect
from .models import iicInfo

def h1(req):
    info = iicInfo.objects.first()
    context = {'iic' : info}
    return render(req, "team.html" , context)