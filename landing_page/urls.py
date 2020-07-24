from django.urls import path,include
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'landing_page'
urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('create-course/', views.CreateCourseView.as_view(), name= "create-course"),
    path('course/<str:slug>/', views.DetailView.as_view(), name='detail'),
    path('course/<str:slug>/edit', views.EditCourseView.as_view(), name="edit-course"),
    path('course/<str:slug>/delete', views.DeleteCourseView.as_view(),name= 'delete-course'),
    path('create-assignment/',views.CreateAssignmentView.as_view(),name='create-assignment'),
    path('assignments/<str:slug>/',views.DocumentView.as_view(),name='assignment-detail'),
    path('assignments/<str:slug>/edit/', views.EditAssignmentView.as_view(), name='edit-assignment'),
]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)