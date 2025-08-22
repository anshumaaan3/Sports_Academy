from django.db import models
from django.utils import timezone


class Notice(models.Model):
    notice_content=models.CharField(max_length=255)
    date=models.DateField(default=timezone.now)





gender =(
    ('male', 'Male'),
    ('female', 'Female'),
   
)
class AdmissionForm(models.Model):
    course_name=models.CharField(max_length=60)
    user_email=models.EmailField(max_length=60,primary_key=True)
    full_name=models.CharField(max_length=60,default="")
    date_of_birth=models.CharField(max_length=10)
    phone=models.CharField(max_length=13)
    gender=models.CharField(max_length=6,choices=gender)
    address=models.TextField(default="")
    admission_status=models.CharField(max_length=10,default="pending")
    pic_name=models.FileField(upload_to="admission_pic/")

class Contact(models.Model):
    name=models.CharField(max_length=40,null=False)
    email=models.EmailField(max_length=40,null=False)
    phone=models.CharField(max_length=13,null=False)
    query=models.TextField(default='')
    date=models.DateField(default=timezone.now)

class FeedBack(models.Model):
    name=models.CharField(max_length=40,null=False)
    email=models.EmailField(max_length=40,null=False,primary_key=True)
    rating=models.CharField(max_length=5,null=False)
    remarks=models.TextField(default='')
    date=models.DateField(default=timezone.now)   

class User(models.Model):
    name=models.CharField(max_length=40,null=False)
    email=models.EmailField(max_length=40,null=False,primary_key=True)
    password=models.CharField(max_length=40,null=False)
    phone=models.CharField(max_length=50,null=False)
    profile_pic=models.FileField( upload_to ="user_pic/",default="")
    date=models.DateField(default=timezone.now) 

class SportsCourse(models.Model):
    sports_name=models.CharField(max_length=40,null=False)
    duration=models.CharField(max_length=40,null=False,)
    charges=models.CharField(max_length=40,null=False)
    phone=models.CharField(max_length=50,null=False)
    description=models.CharField(max_length=500,null=False)
    sports_pic=models.FileField(upload_to="SportsCourse_pic/",default="")
    date=models.DateField(default=timezone.now) 

class Coach(models.Model):
    name=models.CharField(max_length=40,null=False)
    email=models.EmailField(max_length=40,null=False,primary_key=True)
    age=models.CharField(max_length=40,null=False)
    phone=models.CharField(max_length=50,null=False)
    experience=models.CharField(max_length=50,null=False)
    sport_name=models.CharField(max_length=50,null=False)
    profile_pic=models.FileField( upload_to ="coach_pic/",default="")
    date=models.DateField(default=timezone.now) 

