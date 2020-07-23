from django.contrib import admin
from django.urls import include, path

from landing_page import views

app_name = 'main'
urlpatterns = [
    path('', include('landing_page.urls')),
    path('admin/', admin.site.urls),
    path('register/', views.register_page, name= "register" ),
    path('accounts/',include('django.contrib.auth.urls'))
    ]


