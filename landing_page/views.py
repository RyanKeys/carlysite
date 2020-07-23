from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Course
from .forms import CreateUserForm, FileFieldForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth import login,logout,authenticate
from django.views.generic.edit import FormView


class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'upload.html'  # Replace with your template.
    success_url = '...'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                ...  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
def register_page(request):
    if request.user.is_authenticated:
        return redirect('landing_page:index')
    else:
        form = CreateUserForm()
        if request.method =='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
        context = {'form':form}
        return render(request,'registration/register.html',context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('landing_page:index')
    else:
        context = {}
        return render(request,'registration/login.html',context)

def logout_page(request):
    logout(request)
    return redirect('login')

class IndexView(LoginRequiredMixin,generic.ListView):
    template_name = 'landing_page/index.html'
    context_object_name = 'courses'

    def get_queryset(self):
        """Return the last five published questions (not including those set to be
        published in the future)."""
        return Course.objects.all()



class DetailView(LoginRequiredMixin,generic.DetailView):
    model = Course
    template_name = 'landing_page/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Course.objects.filter(pub_date__lte=timezone.now())

class DocumentView(LoginRequiredMixin,generic.DetailView):
    model = Course
    template_name = 'landing_page/document_viewer.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Course.objects.filter(pub_date__lte=timezone.now())