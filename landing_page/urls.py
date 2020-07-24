from django.urls import path,include
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'landing_page'
urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('course/<str:slug>/', views.DetailView.as_view(), name='detail'),
    path('create-course/', views.CreateCourseView.as_view(), name= "create-course"),
    path('course/<str:slug>/delete', views.DeleteItem.as_view()),
    path('assignments/<str:slug>',views.DocumentView.as_view(),name='assignment-detail')
]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)