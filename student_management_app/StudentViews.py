import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from student_management_app.models import Parents, Courses, Subjects, CustomUser, Attendance, Attendance_Report

def student_home(request):
    return render(request,"parent_template/student_home_template.html")
def student_view_attendance(request):
    return render(request,"parent_template/student_view_attendance.html")
