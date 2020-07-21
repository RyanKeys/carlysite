from django.db import models
import datetime
from django.utils import timezone
import uuid


class Student(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Assignment(models.Model):
    assignment_name = models.CharField(max_length=50)
    url = models.URLField(max_length=200)

class Course(models.Model):
    class_name = models.CharField(max_length=50)
    teacher = models.ForeignKey("Teacher", null=True,on_delete=models.SET_NULL)
    students = models.ManyToManyField(Student)
    assignments = models.ForeignKey('Assignment',null=True,on_delete=models.SET_NULL)
    zoom  = models.URLField(max_length=200)
    