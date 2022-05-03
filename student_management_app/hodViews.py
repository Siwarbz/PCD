
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from student_management_app.models import CustomUser, Teachers,Class

def admin_home(request):
    return render(request, "hod_template/home_content.html")


def add_teacher(request):
    return render(request, "hod_template/add_teacher_template.html")


def add_teacher_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                  password=password, email=email, user_type=2)
            user.teachers.address = address
            user.save()
            messages.success(request, "Teacher is Sucessfully Added")

            return HttpResponseRedirect("/add_teacher")

        except:
            messages.error(request, "Failed to add a teacher")
            return HttpResponseRedirect("/add_teacher")


def exam_calendar(request):
    return render(request, "hod_template/exam_calendar.html")


def add_class(request):
    return render(request, "hod_template/add_class_template.html")


def add_class_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        class_name = request.POST.get("class_name")
        level = request.POST.get("level")

        try:
            classe = Class(class_name=class_name, level=level)
            classe.save()
            messages.success(request, "Class is Sucessfully Added")

            return HttpResponseRedirect("/add_class")

        except:
            messages.error(request, "Failed to add a class")
            return HttpResponseRedirect("/add_class")


def add_parent(request):
    classes = Class.objects.all()
    return render(request, "hod_template/add_parent_template.html", {"classes": classes})


def add_parent_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        address = request.POST.get("address")
        kid_name = request.POST.get("kid_name")
        kid_gender = request.POST.get("kid_gender")
        session_start_year = request.POST.get("session_start_year")
        session_end_year = request.POST.get("session_end_year")
        class_id = request.POST.get("class_id")
        try:
            user = CustomUser.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                              password=password, email=email, user_type=3)
            user.parents.address = address
            class_obj = Class.objects.get(id=class_id)
            user.parents.kid_name = kid_name
            user.parents.kid_gender = kid_gender
            user.parents.session_start_year = session_start_year
            user.parents.session_end_year = session_end_year
            user.parents.class_id = class_obj
            user.save()
            messages.success(request, "Parent is Sucessfully Added")

            return HttpResponseRedirect("/add_parent")

        except:
           messages.error(request,"Failed to add a parent")
           return HttpResponseRedirect("/add_parent")