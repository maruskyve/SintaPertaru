"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from . import views, services

urlpatterns = [
    path(r'', views.view_index, name='view_index'),
    path(r'dashboard', views.view_dashboard, name='view_dashboard'),
    path(r'dashboard/login=<int:login>', views.view_dashboard, name='view_dashboard'),  # Login check
    # path(r'dashboard', views.view_dashboard, name='view_dashboard'),  # Login check
    path(r'login', views.view_login, name='view_login'),
    path(r'login/signup=<int:signup>', views.view_login, name='view_login'),
    path(r'login/login=<int:login>', views.view_login, name='view_login'),
    path(r'signup', views.view_signup, name='view_signup'),
    path(r'gis_service', views.view_gis_service, name='view_gis_service'),
    path(r'ls', views.view_ls, name='view_ls'),
    path(r'ls/csvexport/dtype=<str:data_type>', views.view_export_csv, name='view_export_csv'),
    path(r'guest_book', views.view_guest_book, name='view_guest_book'),
    path(r'my_profile', views.view_user_profile, name='view_user_profile'),
    path(r'help', views.view_help, name='view_help'),
    path(r'info', views.view_info, name='view_info'),

    # App Additional Services
    path(r'logout', services.GeneralServices.service_logout, name='service_logout'),

    # URL Exception Handler
    path(r'err404', views.view_err404, name='view_err404'),
]
