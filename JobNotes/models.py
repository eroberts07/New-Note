from email.utils import format_datetime
from django.db import models
from django import forms
import re
from django.db.models.deletion import CASCADE
import bcrypt

class UserManager(models.Manager):
    def register_validator(self, PostData):
        errors={}
        if len(PostData['first_name'])<1:
            errors['first_name']='Name is required'
            
        if  PostData['first_name'].isalpha() == False:
            errors['first_name']='Please ender only letters for your name.'

        if len(PostData['password'])<8:
            errors['password']='Your password must be at least 8 characters'

        elif PostData['password'] != PostData['confirm']:
            errors['password']='Passwords do not match!'

        if len(PostData['email'])<1:
            errors['email']='Email is required'

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not EMAIL_REGEX.match(PostData['email']):    # test whether a field matches the pattern            
            errors['email'] = ("Invalid email address!")

        elif len(User.objects.filter(email=PostData['email']))>0:
            errors['email']='That email already exists!'
        return errors


    def login_validator(self, PostData):
        existing_users= User.objects.filter(email=PostData['email'])
        errors={}
        if len(PostData['email'])<1:
            errors['email']='Email Required'
        
        if len(User.objects.filter(email=PostData['email']))==0:
            errors['email']= 'Please enter a valid email and password'
        elif len(PostData['password'])<8:
            errors['password']= 'Password required'

        elif not bcrypt.checkpw(PostData['password'].encode(), existing_users[0].password.encode()):
            errors['mismatch'] = 'Please enter a valid email and password'

        return errors

class JobManager(models.Manager):
    def job_validator(self, PostData):
        errors={}
        if len(PostData['title'])<1:
            errors['title']='Title is required'
        
        elif len(PostData['title'])<3:
            errors['title']='Title must be 3 characters long'
        
        if len(PostData['description'])<1:
            errors['description']='Description is required'
        
        elif len(PostData['description'])<3:
            errors['description']='Description must be at least 3 characters long'
        
        if len(PostData['location'])<1:
            errors['locaiton']='Location is required'
        
        elif len(PostData['location'])<3:
            errors['location']='Location must be at least 3 characters long'
        return errors

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

class Vehicle(models.Model):
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Equipment(models.Model):
    name=models.CharField(max_length=255)
    quantity= models.PositiveIntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Task(models.Model):
    name=models.CharField(max_length=255,blank=True)
    description=models.TextField(blank=True)
    timein=models.TimeField(blank=True, null=True)
    timeout=models.TimeField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Job(models.Model):
    title=models.CharField(max_length=255)
    date=models.DateField(default=0)
    description=models.TextField()
    location=models.CharField(max_length=255)
    uploader=models.ForeignKey(User, related_name='jobs_uploaded', on_delete=CASCADE)
    workers=models.IntegerField()
    vehicles=models.IntegerField()
    equipment=models.CharField(max_length=255)
    my_jobs=models.ManyToManyField(User, related_name='active_jobs')
    #vehicles=models.ManyToManyField(Vehicle, related_name='vehicles', blank=True)
    #equipment=models.ManyToManyField(Equipment, related_name='equipment_used')
    tasks=models.ManyToManyField(Task,related_name='active_tasks')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=JobManager()
