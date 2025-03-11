"""
URL configuration for taskmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from tasks.views import register  # Import your registration view
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # This includes your tasks app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Provides login, logout, password change/reset
    path('accounts/register/', register, name='register'),
    # Override password change views to force custom templates:
    # path('accounts/password_change/', 
    #      auth_views.PasswordChangeView.as_view(
    #          template_name='registration/password_change_form.html'
    #      ), 
    #      name='password_change'),
    # path('accounts/password_change/done/', 
    #      auth_views.PasswordChangeDoneView.as_view(
    #          template_name='registration/password_change_done.html'
    #      ), 
    #      name='password_change_done'),
    # path('accounts/', include('accounts.urls')),  # user registration
    # path('api/', include('api.urls')),  # API
]