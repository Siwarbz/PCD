"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from student_management_app import views, hodViews
from django.contrib import admin
from django.conf.urls.static import static
from student_management_system import settings
from django.urls import path



urlpatterns = [
    path('demo',views.showDemoPage),
    path('admin/', admin.site.urls),
    path('',views.ShowLoginPage),
    path('get_user_details',views.GetUserDetails),
    path('logout_user',views.logout_user),
    path('doLogin',views.doLogin),
    path('admin_home',hodViews.admin_home),
    path('add_teacher',hodViews.add_teacher),
    path('add_teacher_save',hodViews.add_teacher_save),
    path('exam_calendar',hodViews.exam_calendar),
    path('add_class',hodViews.add_class),
    path('add_class_save',hodViews.add_class_save),
    path('add_parent',hodViews.add_parent),
    path('add_parent_save',hodViews.add_parent_save),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
