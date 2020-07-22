from django.db import models
import datetime
from django.utils import timezone
from django.utils.text import slugify


class Student(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Assignment(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    def __str__(self):
        return self.name

def slugger(teacher,class_name):
    return sluggify()
class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200,blank=True)
    teacher = models.ForeignKey("Teacher", null=True,on_delete=models.SET_NULL)
    students = models.ManyToManyField(Student)
    assignments = models.ManyToManyField(Assignment)
    zoom  = models.URLField(max_length=200)
    pub_date = models.DateTimeField("date published", null=True)
    slug = models.SlugField(unique=True,editable=False)
    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        self.slug = slugify([self.teacher.name,self.name])
        super(Course,self).save(*args, **kwargs)

    