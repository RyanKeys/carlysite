from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

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
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    slug = models.CharField(max_length=50,unique= True,blank=True,editable=False)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """ Returns path for a listing """
        path_components = {'slug': self.slug}
        return reverse('landing_page/assignment-detail', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        self.slug = slugify(self.document, allow_unicode=True)

        return super(Assignment, self).save(*args, **kwargs)
   
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

    