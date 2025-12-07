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
    description = models.TextField(max_length = 1000 , blank = False)
    date = models.DateTimeField(auto_now = True)
    photo = models.ImageField(upload_to='image/achievements/', null=True , blank = True)
    pdf_file = models.FileField(upload_to='pdfs/', null=True , blank = True)

    def __str__(self):
        return self.title
    
class meeting(models.Model):
    date = models.DateTimeField()
    headline = models.CharField(max_length = 100, blank = True)
    description = models.TextField()
    faculty = models.ManyToManyField(facult , blank = True , null = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.headline
    
class notice(models.Model):
    date = models.DateTimeField(auto_now = True)
    headline = models.CharField(max_length = 100, blank = True)
    description = models.TextField()
    pdf_file = models.FileField(upload_to='pdfs/', null=True , blank = True)
    photo = models.ImageField(upload_to='image/notices/', null=True , blank = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.headline

class activity(models.Model):
    class cat(models.TextChoices):
        IIC_Calender = "IIC Calender Activity"
        MIC_Driven = "MIC_Driven Activity"
        Celebration = "Celebration Activity"
        Self_Driven = "Self Driven Activity"
    date = models.DateTimeField()
    headline = models.CharField(max_length = 100, blank = True)
    category = models.CharField(choices = cat , null = True , blank = True , max_length = 25)
    photo = models.ImageField(upload_to='image/activities/', null=True , blank = True)
    pdf_file = models.FileField(upload_to='pdfs/', null=True , blank = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.headline
    
class gallery(models.Model):
    photo = models.ImageField(upload_to='image/gallery/', null=True , blank = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.photo)
    
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
    
class iicInfo(models.Model):
    navLogo = models.ImageField(blank = True , null = True)
    logo = models.ImageField(blank = True , null = True)
    home = models.ImageField(blank = True , null = True)
    email = models.EmailField(blank = False , null = False)
    phone = models.CharField(max_length = 11 , blank = False , null = False)

    def __str__(self):
        return "Email Info"