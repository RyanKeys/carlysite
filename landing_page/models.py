from django.db import models
import datetime
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User, Group

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    drive = models.URLField(max_length=50,blank=False)

    def __str__(self):
        return self.user.username

   


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    drive = models.URLField(max_length=50,blank=False)
    def __str__(self):
        return self.user.username  

class Assignment(models.Model):
    name = models.CharField(max_length=50)
    document = models.FileField(null=True,blank=True)
    def __str__(self):
        return self.name

def slugger(teacher,class_name):
    return sluggify()

    
class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200,blank=True)
    teacher = models.ForeignKey(Teacher, null=True,on_delete=models.SET_NULL)

    students = models.ManyToManyField(Student)
    assignments = models.ManyToManyField(Assignment)
    zoom  = models.URLField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    slug = models.SlugField(unique=True,editable=True,blank=True)
    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        print(self.slug)
        if self.slug == "":
            self.slug = slugify([self.teacher.user.username,self.name])
        super(Course,self).save(*args, **kwargs)

    