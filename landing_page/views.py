from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Course, Assignment
from .forms import CreateUserForm, FileFieldForm,CourseForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth import login,logout,authenticate
from django.views.generic.edit import FormView, DeleteView



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
    model = Assignment
    def get(self,request,slug):
        
        assignment = self.get_queryset().get(slug__iexact=slug)
        return render(request,'landing_page/document_viewer.html',{'assignment': assignment })


class CreateCourseView(FormView):
    form_class = CourseForm
    template_name = 'landing_page/form_upload.html'  # Replace with your template.
    success_url = '/'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class DeleteItem(DeleteView):
    model = Course
    template_name = 'item_delete.html'

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Course, slug=slug)

    def get_success_url(self):
        return reverse('detail')

        