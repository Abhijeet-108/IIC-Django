from django.db import models

# Create your models here.

class dept(models.Model):
    name = models.CharField(max_length = 100 , blank = False , null = False)

    def __str__(self):
        return self.name
    
class suff(models.Model):
    pre = models.CharField(max_length = 10 , blank = False , null = False)

    def __str__(self):
        return self.pre

class facult(models.Model):
    dept = models.ForeignKey(dept , on_delete = models.CASCADE)
    suf = models.ForeignKey(suff , on_delete = models.CASCADE)
    name = models.CharField(max_length = 30 , blank = False)
    email = models.EmailField(blank = True)

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
    year = models.IntegerField(blank = True)
    stat = models.CharField(max_length = 40 , choices = status , null = True , blank = True)

    def __str__(self):
        return str(self.patentNumber) + "  " + self.title
    
class book(models.Model):
    faculty = models.ForeignKey(facult , on_delete = models.CASCADE)
    title = models.CharField(max_length = 500 , blank = True)
    authors = models.CharField(max_length = 1000 , blank = True)
    isbn = models.CharField(max_length = 30 , blank = True)
    publisherName = models.CharField(max_length = 200 , blank = True)
    year = models.IntegerField(blank = True)

    def __str__(self):
        return self.isbn + " " + self.title
    
class bookChapter(models.Model):
    faculty = models.ForeignKey(facult , on_delete = models.CASCADE)
    title = models.CharField(max_length = 500 , blank = True)
    authors = models.CharField(max_length = 1000 , blank = True)
    isbn = models.CharField(max_length = 30 , blank = True)
    chapterName = models.CharField(max_length = 300 , blank = True)
    pageNo = models.CharField(max_length = 50 , blank = True)
    doiLink = models.CharField(max_length = 500 , blank = True)
    publisherName = models.CharField(max_length = 200 , blank = True)
    year = models.IntegerField(blank = True)

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
    year = models.IntegerField(blank = True)
    stat = models.CharField(max_length = 40 , choices = status , null = True , blank = True)

    def __str__(self):
        return self.copyrightNumber + " " + self.title
    
class journal(models.Model):
    faculty = models.ForeignKey(facult , on_delete = models.CASCADE)
    title = models.CharField(max_length = 500 , blank = True)
    authors = models.CharField(max_length = 1000 , blank = True)
    isbn = models.CharField(max_length = 30 , blank = True)
    journalName = models.CharField(max_length = 200 , blank = True)
    publisherName = models.CharField(max_length = 200 , blank = True)
    issue = models.CharField(max_length = 20 , blank = True)
    no = models.CharField(max_length = 20 , blank = True)
    pageNo = models.CharField(max_length = 20 , blank = True)
    year = models.IntegerField(blank = True)
    doiLink = models.CharField(max_length = 500 , blank = True)

    def __str__(self):
        return self.journalName
    
class conference(models.Model):
    faculty = models.ForeignKey(facult , on_delete = models.CASCADE)
    title = models.CharField(max_length = 500 , blank = True)
    authors = models.CharField(max_length = 1000 , blank = True)
    issn = models.CharField(max_length = 30 , blank = True)
    journalName = models.CharField(max_length = 200 , blank = True)
    publisherName = models.CharField(max_length = 200 , blank = True)
    issue = models.CharField(max_length = 20 , blank = True)
    no = models.CharField(max_length = 20 , blank = True)
    pageNo = models.CharField(max_length = 20 , blank = True)
    year = models.IntegerField(blank = True)
    doiLink = models.CharField(max_length = 500 , blank = True)

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