from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class dept(models.Model):
    name = models.CharField(max_length = 100 , unique = True , blank = False , null = False)

    def __str__(self):
        return self.name
    
class suff(models.Model):
    pre = models.CharField(max_length = 10 , blank = False , null = False)

    def __str__(self):
        return self.pre

class facult(models.Model):
    class qual(models.TextChoices):
        Post_Graduate = "Post Graduate"
        Doctorate = "Doctorate"


    user = models.ForeignKey(User, on_delete = models.CASCADE , blank = True , null = True)
    dept = models.ForeignKey(dept , on_delete = models.CASCADE)
    suf = models.ForeignKey(suff , on_delete = models.CASCADE)
    name = models.CharField(max_length = 30 , blank = False)
    photo = models.ImageField(blank = True , null = True)
    email = models.EmailField(blank = True)
    phone = models.CharField(max_length = 11 ,blank = True , null = True)
    qualification = models.CharField(choices = qual , null = True , blank = True)
    role = models.CharField(blank = True , null = True)
    experience = models.IntegerField(max_length = 2 , null = True , blank = True)

    def __str__(self):
        return self.name
    
class patent(models.Model):
    class status(models.TextChoices):
        Published = "Published"
        Granted = "Granted"

    faculty = models.ForeignKey(facult , on_delete = models.CASCADE)
    patentNumber = models.CharField(max_length=50 , unique=True , blank = True , null = True)
    area = models.CharField(max_length=100 , blank = True , null = True)
    domain = models.CharField(max_length=100 , blank = True , null = True)
    title = models.CharField(max_length=200 , blank = True , null = True)
    year = models.IntegerField(blank = True , null = True)
    stat = models.CharField(max_length = 40 , choices = status , null = True , blank = True)
    support = models.FileField(upload_to='rnd/pdfs/', null = True , blank = True)

    def __str__(self):
        return str(self.patentNumber) + "  " + self.title
    
class book(models.Model):
    faculty = models.ForeignKey(facult , on_delete = models.CASCADE)
    title = models.CharField(max_length = 500 , blank = True , null = True)
    authors = models.CharField(max_length = 1000 , blank = True , null = True)
    isbn = models.CharField(max_length = 30 , blank = True , null = True)
    publisherName = models.CharField(max_length = 200 , blank = True , null = True)
    year = models.IntegerField(blank = True , null = True)
    support = models.FileField(upload_to='rnd/pdfs/', null = True , blank = True)

    def __str__(self):
        return self.isbn + " " + self.title
    
class bookChapter(models.Model):
    faculty = models.ForeignKey(facult , on_delete = models.CASCADE)
    title = models.CharField(max_length = 500 , blank = True , null = True)
    authors = models.CharField(max_length = 1000 , blank = True , null = True)
    isbn = models.CharField(max_length = 30 , blank = True , null = True)
    chapterName = models.CharField(max_length = 300 , blank = True , null = True)
    pageNo = models.CharField(max_length = 50 , blank = True , null = True)
    doiLink = models.CharField(max_length = 500 , blank = True , null = True)
    publisherName = models.CharField(max_length = 200 , blank = True , null = True)
    year = models.IntegerField(blank = True , null = True)
    support = models.FileField(upload_to='rnd/pdfs/', null = True , blank = True)

    def __str__(self):
        return self.title + " " + self.chapterName

class copyright(models.Model):
    class status(models.TextChoices):
        Registered = "Registered"
        Pending = "Pending"
        Reviewing = "Under Review"
    faculty = models.ForeignKey(facult , on_delete = models.CASCADE)
    copyrightNumber = models.CharField(max_length=50 , unique=True , blank = True , null = True)
    area = models.CharField(max_length=100 , blank = True , null = True)
    domain = models.CharField(max_length=100 , blank = True , null = True)
    title = models.CharField(max_length=200 , blank = True , null = True)
    year = models.IntegerField(blank = True , null = True)
    stat = models.CharField(max_length = 40 , choices = status , null = True , blank = True)
    support = models.FileField(upload_to='rnd/pdfs/', null = True , blank = True)

    def __str__(self):
        return self.copyrightNumber + " " + self.title
    
class journal(models.Model):
    faculty = models.ForeignKey(facult , on_delete = models.CASCADE)
    title = models.CharField(max_length = 500 , blank = True , null = True)
    authors = models.CharField(max_length = 1000 , blank = True , null = True)
    isbn = models.CharField(max_length = 30 , blank = True , null = True)
    journalName = models.CharField(max_length = 200 , blank = True , null = True)
    publisherName = models.CharField(max_length = 200 , blank = True , null = True)
    issue = models.CharField(max_length = 20 , blank = True , null = True)
    no = models.CharField(max_length = 20 , blank = True , null = True)
    pageNo = models.CharField(max_length = 20 , blank = True , null = True)
    year = models.IntegerField(blank = True , null = True)
    doiLink = models.CharField(max_length = 500 , blank = True , null = True)
    support = models.FileField(upload_to='rnd/pdfs/', null = True , blank = True)

    def __str__(self):
        return self.journalName
    
class conference(models.Model):
    faculty = models.ForeignKey(facult , on_delete = models.CASCADE)
    title = models.CharField(max_length = 500 , blank = True , null = True)
    authors = models.CharField(max_length = 1000 , blank = True , null = True)
    issn = models.CharField(max_length = 30 , blank = True , null = True)
    journalName = models.CharField(max_length = 200 , blank = True , null = True)
    publisherName = models.CharField(max_length = 200 , blank = True , null = True)
    issue = models.CharField(max_length = 20 , blank = True , null = True)
    no = models.CharField(max_length = 20 , blank = True , null = True)
    pageNo = models.CharField(max_length = 20 , blank = True , null = True)
    year = models.IntegerField(blank = True , null = True)
    doiLink = models.CharField(max_length = 500 , blank = True , null = True)

    def __str__(self):
        return self.journalName
    
class basicDetails(models.Model):
    faculty = models.ForeignKey(facult , on_delete = models.CASCADE)
    googleScholar = models.CharField(max_length = 500 , null = True , blank = True)
    orcid = models.CharField(max_length = 50 , null = True , blank = True)
    scopusid = models.CharField(max_length = 50 , null = True , blank = True)
    researchid = models.CharField(max_length = 50 , null = True , blank = True)
    vidwanPortal = models.CharField(max_length = 500 , null = True , blank = True)

    def __str__(self):
        return str(self.faculty) + "  Basics"