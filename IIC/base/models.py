from django.db import models
from rnd.models import facult

# Create your models here.

class posts(models.Model):
    title = models.CharField(max_length= 80 , blank = False)
    description = models.CharField(max_length = 1000 , blank = False)

    def __str__(self):
        return self.title
    
class achievement(models.Model):
    title = models.CharField(max_length = 100 , blank = True)
    description = models.TextField()
    date = models.DateTimeField(auto_now = True)
    photo = models.ImageField(blank = True)

    def __str__(self):
        return self.title
    
class event(models.Model):
    class status(models.TextChoices):
        Notice = "Notice"
        Activity = "Activity"
        Meeting = "Meeting"
    date = models.DateTimeField(auto_now = True)
    headline = models.CharField(max_length = 100, blank = True)
    description = models.TextField()
    stat = models.CharField(max_length = 30 , choices = status)
    faculty = models.ManyToManyField(facult , blank = True , null = True)

    def __str__(self):
        return self.headline
    
class contactOrg(models.Model):
    name = models.CharField(max_length = 100 , blank = False , null = False)
    designation = models.CharField(max_length = 100 , blank = False , null = False)
    email = models.EmailField(blank = False , null = False)
    phone = models.CharField(max_length = 15 , unique = True)
    website = models.CharField(max_length = 256 , null = True , blank = True)

    def __str__(self):
        return self.name
    
class organisation(models.Model):
    class stages(models.TextChoices):
        Ideation = "Ideation]"
        Validation = "Validation"
        Early_Traction = "Early Traction"
        Scaling = "Scaling"
        Maturity = "Maturity"

    class status(models.TextChoices):
        Incubator = "Incubator"
        Startup = "Startup"

    name = models.CharField(max_length = 100 , blank = True , null = True)
    thrustArea = models.CharField(max_length = 500 , blank = True , null = True)
    city = models.CharField(max_length = 100 , blank = False , null = False)
    address = models.TextField()
    contact = models.ManyToManyField(contactOrg)
    stage = models.CharField(max_length = 20 , choices = stages , blank = True , null = True)
    stat = models.CharField(max_length = 20 , choices = status , blank = True , null = True)

    def __str__(self):
        return self.name
    
class querys(models.Model):
    class sub(models.TextChoices):
        Gen = "General Inquiry"
        Mem = "IIC Membership"
        PS = "Project Support"
        Competition = "Competition Information"
        Other = "Other"
    fullname = models.CharField(max_length = 70 , null = False , blank = False)
    email = models.EmailField(blank = False , null = False)
    phone = models.CharField(max_length = 11 , blank = False , null = False)
    message = models.TextField(blank = False , null = False)
    subject = models.CharField(choices = sub , max_length = 70 , null = False , blank = False)

    def __str__(self):
        return self.subject + " " + self.fullname