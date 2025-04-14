"""
URL configuration for olympicgym project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register.views import register_request, login_request, logout_request, update_profile, profile
from workout import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('workout/', include('workout.urls')),
    path('', views.home, name='home' ), # home
    path('register/', register_request, name="register"), # register 
    path('profile/', profile, name="profile"),  # profile  
    path('profile/update/', update_profile, name="update_profile"), # profile update
    path('login/', login_request, name="login"),  # login
    path('logout/', logout_request, name="logout"), # logout
]
