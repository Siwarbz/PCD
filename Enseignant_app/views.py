from distutils import core
from http.client import HTTPResponse
import json
from django.shortcuts import render
from Enseignant_app.models import Subjects  
from Enseignant_app.models import Classe
from Enseignant_app.models import Courses
from Enseignant_app.models import Homework
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from Enseignant_app.models import Students

# Create your views here.
def teacher_home(request):
    return render(request,"teacher_template/teacher_home.html")

def teacher_take_attendance(request):
    subjects=Subjects.objects.all() 
    classes=Classe.objects.all()
    return render(request, "teacher_template/teacher_take_attendance.html", {"subjects":subjects, "classes":classes})

@csrf_exempt
def teacher_add_homework(request): 
    subjects=Subjects.objects.all() 
    classes=Classe.objects.all()
    if request.method == 'POST':
        classe_name = request.POST.get('classe_name')
        subject_name = request.POST.get('subject_name')
        file = request.POST.get('file')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')
        newHomework = Homework.objects.create(subject_name=subject_name, classe_name=classe_name,file=file,description=description,deadline=deadline)
        newHomework.save()
    return render(request,"teacher_template/teacher_add_homework.html", {"subjects":subjects, "classes":classes})

def teacher_add_course(request): 
    subjects=Subjects.objects.all() 
    classes=Classe.objects.all()
    if request.method == 'POST':
        course_name='course'
        classe_name= request.POST.get('classe_name')
        subject_name= request.POST.get('subject_name')
        file = request.POST.get('file')
        description = request.POST.get('description')
        newCourse = Courses.objects.create(course_name=course_name,file=file,description=description,classe_name=classe_name,subject_name=subject_name)
        newCourse.save()
    return render(request,"teacher_template/teacher_add_course.html", {"subjects":subjects, "classes":classes})
def students_list(request):
    students=Students.objects.all()
    classes=Classe.objects.all()
    return render(request,"teacher_template/students_list.html",{"students":students,"classes":classes})
    


@csrf_exempt
def get_students(request): 
    subject_id = request.POST.get("subject")
    classe_id = request.POST.get("classe")
    students=Students.objects.filter(classe_id=classe_id) 
    student_data=serializers.serialize("python", students)

    list_data=[]

    for student in students:
        data_small={"id":student.id, "name": student.name}
        list_data.append(data_small)


    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)

@csrf_exempt
def save_attendance_data(request):
    student_ids=request.POST.getlist("student_ids[]")
    print(student_ids)
    return HTTPResponse("OK") 

@csrf_exempt
def get_students_list(request): 
    classe_id = request.POST.get("classe")
    students=Students.objects.filter(classe_id=classe_id) 
    student_data=serializers.serialize("python", students)

    list_data=[]

    for student in students:
        data_small={"id":student.id, "name": student.name}
        list_data.append(data_small)


    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)

