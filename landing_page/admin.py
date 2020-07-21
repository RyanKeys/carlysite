# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Assignment)
admin.site.register(Course)
