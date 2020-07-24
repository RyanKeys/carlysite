from django.forms import ModelForm
from .models import Course, Assignment
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User




class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","username",'email','password1','password2']