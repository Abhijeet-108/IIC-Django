from django.db import models
from rnd.models import facult

# Create your models here.

class posts(models.Model):
    title = models.CharField(max_length= 80 , blank = False)
    description = models.CharField(max_length = 1000 , blank = False)

    def __str__(self):
        return self.title
    
class achievement(models.Model):
    class status(models.TextChoices):
        Approved = "Approved"
        Pending = "Pending"
    title = models.CharField(max_length = 100 , blank = True)
    description = models.TextField(max_length = 1000 , blank = False)
    date = models.DateField(null=True , blank = True)
    time = models.TimeField(null=True , blank = True)
    stat = models.CharField(choices = status , default = status.Pending , null = True , blank = True)
    photo = models.ImageField(upload_to='image/achievements/', null=True , blank = True)
    pdf_file = models.FileField(upload_to='pdfs/', null=True , blank = True)

    def __str__(self):
        return self.title
    
class meeting(models.Model):
    date = models.DateField(null=True , blank = True)
    time = models.TimeField(null=True , blank = True)
    headline = models.CharField(max_length = 100, blank = True)
    description = models.TextField()
    support = models.FileField(upload_to='meeting/pdfs/', null=True , blank = True)
    faculty = models.ManyToManyField(facult , blank = True , null = True)
    support = models.FileField(upload_to='meeting/pdfs/', null=True , blank = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.headline
    
class notice(models.Model):
    headline = models.CharField(max_length = 100, blank = True)
    description = models.TextField()
    pdf_file = models.FileField(upload_to='pdfs/', null=True , blank = True)
    photo = models.ImageField(upload_to='image/notices/', null=True , blank = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.headline

class activity(models.Model):
    class cat(models.TextChoices):
        IIC_Calender = "IIC Calender Activity"
        MIC_Driven = "MIC Driven Activity"
        Celebration = "Celebration Activity"
        Self_Driven = "Self Driven Activity"
    date = models.DateField(null=True , blank = True)
    time = models.TimeField(null=True , blank = True)
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
    
class teamMember(models.Model):
    class role(models.TextChoices):
        Convenor = "Convenor"
        Co_Convenor = "Co-Convenor"
        Convenor_External = "Convenor of External Affairs"
        Director_Operations_Head = "Hult Prize Campus Director & Operations Head"
        Chief_Financial = "Chief Financial & Strategic Advisor"
        Head_Tech_Wing = "Head of Tech Wing"
        Co_Head_Tech_Wing = "Co-Head of Tech Wing"
        Head_Graphics_Wing = "Head of Graphics Wing"
        Co_Head_Graphics_Wing = "Co-Head of Graphics Wing"
        Head_Startup_Wing = "Head of Startup Wing"
        Co_Head_Startup_Wing = "Co-Head of Startup Wing"
        Head_PR_Outreach_Wing = "Head of Public Relations And Outreach wing"
        Co_Head_PR_Outreach_Wing = "Co-Head of Public Relations And Outreach wing"
        Head_management_Wing = "Head of Management and Resource wing"
        Co_Head_management_Wing = "Co-Head of Management and Resource wing"
        Head_Social_Media_Wing = "Head of Social Media Wing"
        Co_Head_Social_Media_Wing = "Co-Head of Social Media Wing"
        Head_Sponsorship_Wing = "Head of Sponsorship Wing"
        Co_Head_Sponsorship_Wing = "Co-Head of Sponsorship Wing"
        Head_content_Wing = "Head of Content Wing"
        Co_Head_content_Wing = "Co-Head of Content Wing"
        
    role = models.CharField(max_length=100, choices=role.choices, blank=True, null=True,)
    name = models.CharField(max_length = 100 , blank = False , null = False)
    email = models.EmailField(blank = False , null = False)
    photo = models.ImageField(upload_to='member/images/',blank = True , null = True)
    support = models.FileField(upload_to='member/pdfs/', null = True , blank = True)

    def __str__(self):
        return self.name

class certificate(models.Model):
    name = models.CharField(max_length = 100 , blank = False , null = False)
    photo = models.ImageField(upload_to='certificate/images/',blank = True , null = True)
    support = models.FileField(upload_to='certificate/pdfs/', null = True , blank = True)
    date = models.DateField(auto_now = True)

    def __str__(self):
        return self.name
    
class ipr(models.Model):
    title = models.CharField(max_length = 200 , blank = False , null = False)
    description = models.TextField(blank = False , null = False)
    support = models.FileField(upload_to='ipr/pdfs/', null = True , blank = True)

    def __str__(self):
        return self.title

class incubation(models.Model):
    title = models.CharField(max_length = 200 , blank = False , null = False)
    description = models.TextField(blank = False , null = False)
    support = models.FileField(upload_to='incubation/pdfs/', null = True , blank = True)

    def __str__(self):
        return self.title
