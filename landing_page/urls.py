from django.urls import path,include
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'landing_page'
urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('course/<str:slug>/', views.DetailView.as_view(), name='detail'),
    # path('login/', views.login_page, name= "login" ),
    # path('logout/', views.logout_page,name='logout'),
    # path("assignments/<str:slug>/",views.DocumentView.as_view(),name="assignments")
]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)