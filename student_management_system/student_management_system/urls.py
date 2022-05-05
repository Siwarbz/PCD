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
from student_management_app import views
from django.contrib import admin
from django.conf.urls.static import static
from student_management_system import settings
from django.urls import path
from student_management_app import views, StudentViews, hodViews

urlpatterns = [
    path('demo',views.showDemoPage),
    path('' , views.ShowLoginPage),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user, name="logout"),
    path('dologin', views.doLogin),

    #admin path
    
    path('admin/', admin.site.urls),
    path('admin_home',hodViews.admin_home),
    path('add_teacher',hodViews.add_teacher),
    path('add_teacher_save',hodViews.add_teacher_save),
    path('exam_calendar',hodViews.exam_calendar),
    path('add_class',hodViews.add_class),
    path('add_class_save',hodViews.add_class_save),
    path('add_specification',hodViews.add_specification),
    path('add_specification_save',hodViews.add_specification_save),
    path('add_subject',hodViews.add_subject),
    path('add_subject_save',hodViews.add_subject_save),
    path('add_parent',hodViews.add_parent),
    path('add_parent_save',hodViews.add_parent_save),
    path('manage_teacher',hodViews.manage_teacher),
    path('manage_parent',hodViews.manage_parent),
    path('manage_class',hodViews.manage_class),
    path('manage_subject',hodViews.manage_subject),
    path('manage_specification',hodViews.manage_specification),
    path('time_management',hodViews.time_management),
    path('time_management_save',hodViews.time_management_save),
    path('manage_schedule',hodViews.manage_schedule),
    path('schedule_open',hodViews.schedule_open),
    path('schedule',hodViews.schedule),
    path('add_exam_days',hodViews.add_exam_days),
    path('add_exam_days_save',hodViews.add_exam_days_save),
    path('add_exam',hodViews.add_exam),
    path('add_exam_save',hodViews.add_exam_save),
    path('manage_exam_day',hodViews.manage_exam_day),
    path('manage_exam_open',hodViews.manage_exam_open),
    path('manage_exam',hodViews.manage_exam),
    path('manage_chatbot',hodViews.manage_chatbot),
    path('add_note',hodViews.add_note),
    path('add_note_save',hodViews.add_note_save),
    path('remplir_classe_note',hodViews.remplir_classe_note),
    path('remplir_note_save',hodViews.remplir_note_save),
    path('manage_note',hodViews.manage_note),
    path('manage_note_save',hodViews.manage_note_save),
    path('manage_note_view',hodViews.manage_note_view),

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
    path('chatbot', StudentViews.chatbot),
    path('chatbot_save', StudentViews.chatbot_save),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
