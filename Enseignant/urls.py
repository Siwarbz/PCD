"""Enseignant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from Enseignant_app import views


urlpatterns = [
    path('teacher_home',views.teacher_home, name="teacher_home"),
    path('get_students',views.get_students, name="get_students"),
    path('students_list',views.students_list, name="students_list"),
    path('teacher_take_attendance',views.teacher_take_attendance, name="teacher_take_attendance"),
    path('teacher_add_homework', views.teacher_add_homework, name='teacher_add_homework') ,
    path('teacher_add_course', views.teacher_add_course, name="teacher_add_course"), 
    path('save_attendance_data', views.save_attendance_data, name="save_attendance_data"),
    
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)