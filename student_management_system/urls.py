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

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from student_management_system import settings
from student_management_app import views, StudentViews, hodViews

urlpatterns = [
    path('demo',views.showDemoPage),
    path('admin/', admin.site.urls),
    path('' , views.ShowLoginPage),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user, name="logout"),
    path('dologin', views.doLogin),

    #admin path
    path('admin_home',hodViews.admin_home),
    path('add_teacher',hodViews.add_teacher),
    path('add_teacher_save',hodViews.add_teacher_save),
    path('exam_calendar',hodViews.exam_calendar),
    path('add_class',hodViews.add_class),
    path('add_class_save',hodViews.add_class_save),
    path('add_parent',hodViews.add_parent),
    path('add_parent_save',hodViews.add_parent_save),

    #parent url path
    path('student_home', StudentViews.student_home, name="student_home"),
    path('student_view_attendance', StudentViews.student_view_attendance, name="student_view_attendance"),
    path('student_view_attendance_post', StudentViews.student_view_attendance_post, name="student_view_attendance_post"),
    path('voir_homework', StudentViews.voir_homework, name="voir_homework"),
    path('voir_cours', StudentViews.voir_cours, name="voir_cours"),
    path('afficher_note', StudentViews.afficher_note, name="afficher_note"),
    path('facturation', StudentViews.facturation, name="facturation"),
    path('facturation_save', StudentViews.facturation_save, name="facturation_save"),
    path('feedback', StudentViews.feedback, name="feedback"),
    path('feedback_save', StudentViews.feedback_save, name="feedback_save"),
    path('chatbot', StudentViews.chatbot, name="chatbot"),
    path('chatbot_save', StudentViews.chatbot_save, name="chatbot_save"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
