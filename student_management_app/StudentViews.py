import datetime
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from student_management_app.models import Parents, Courses, Subjects, CustomUser, Attendance, Attendance_Report, Teachers, Homework, Exams, Facturation, FeedBackParent, Chatbot, Class ,  Advertisement

def student_home(request):
    parent_obj=Parents.objects.get(admin=request.user.id)
    attendance_total=Attendance_Report.objects.filter(parent_id=parent_obj).count()
    attendance_present = Attendance_Report.objects.filter(parent_id=parent_obj,status=True).count()
    attendance_absent = Attendance_Report.objects.filter(parent_id=parent_obj,status=False).count()
    course=Courses.objects.get(id=parent_obj.course_id.id)
    subjects=Subjects.objects.filter(course_id=course).count()
    subject_name=[]
    data_present = []
    data_absent = []
    subject_data=Subjects.objects.filter(course_id=parent_obj.course_id)
    for subject in subject_data:
        attendance=Attendance.objects.filter(subject_id=subject.id)
        attendance_present_count=Attendance_Report.objects.filter(attendance_id__in=attendance, status=True, parent_id=parent_obj).count()
        attendance_absent_count = Attendance_Report.objects.filter(attendance_id__in=attendance,status= False, parent_id=parent_obj).count()
        subject_name.append(subject.subject_name)
        data_present.append(attendance_present_count)
        data_absent.append(attendance_absent_count)

        return render(request,"parent_template/student_home_template.html",{"attendance_total": attendance_total,"attendance_present": attendance_present,"attendance_absent": attendance_absent, "subjects":subjects , "data_name":subject_name,"data_present":data_present, "data_absent":data_absent})
def student_view_attendance(request):
    student=Parents.objects.get(admin=request.user.id)
    course=student.course_id
    subjects=Subjects.objects.filter(course_id=course)
    return render(request,"parent_template/student_view_attendance.html",{"subjects":subjects})
def student_view_attendance_post(request):
    subject_id=request.POST.get('subject')
    start_date=request.POST.get('start_date')
    end_date=request.POST.get('end_date')

    start_date_parse=datetime.datetime.strptime(start_date,"%Y-%m-%d").date()
    end_date_parse=datetime.datetime.strptime(end_date,"%Y-%m-%d").date()
    subject_obj=Subjects.objects.get(id=subject_id)
    user_object=CustomUser.objects.get(request.user.id)
    stud_obj=Parents.objects.get(admin=user_object)
    attendance=Attendance.objects.filter(attendance_date__range=(start_date_parse,end_date_parse),subject_id=subject_obj)
    attendance_reports=Attendance_Report.objects.filter(attendance_id__in=attendance,parent_id=stud_obj)


    return HttpResponse ("ok")
def voir_cours(request):
    student = Parents.objects.get(admin=request.user.id)
    classe = student.class_id
    cours = Courses.objects.filter(class_id=classe)
    return render(request, "parent_template/voir_cours.html",{"cours": cours})
def afficher_note(request):
    student = Parents.objects.get(admin=request.user.id)
    classe = student.class_id
    exam = Exams.objects.filter(class_id=classe)
    return render(request, "parent_template/afficher_note.html",{"exam": exam} )
def voir_homework(request):
   student = Parents.objects.get(admin=request.user.id)
   classe = student.class_id
   homework = Homework.objects.filter(class_id=classe)
   return render(request, "parent_template/voir_homework.html", {"homework": homework})
def facturation(request):
    return render(request,"parent_template/facturation.html")
def facturation_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        parent = Parents.objects.get(admin=request.user.id)
        classe= parent.class_id
        carte=request.POST.get("carte")
        password = request.POST.get("password")
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        semestre = request.POST.get("semestre")
        try:
            facture_model=Facturation(numero=carte,mdp=password,kid_name2=nom,kid_name1=prenom,semestre=semestre, parent_id=parent,class_id=classe)
            facture_model.save()
            messages.success(request,"paiement fait ave succés")
            return HttpResponseRedirect(reverse("facturation"))
        except:
            messages.error(request,"Erreur de paiement")
            return HttpResponseRedirect(reverse("facturation"))
def feedback(request):
    parent = Parents.objects.get(admin=request.user.id)
    feedback = FeedBackParent.objects.filter(parent_id=parent)
    return render(request,"parent_template/feedback.html", {"feedback": feedback})

def feedback_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        parent = Parents.objects.get(admin=request.user.id)
        feedback=request.POST.get("feedback")
        date=request.POST.get("start_date")
        try:
            feedback=FeedBackParent(feedback=feedback,created_at=date, parent_id=parent)
            feedback.save()
            messages.success(request,"feedback envoyé")
            return HttpResponseRedirect(reverse("feedback"))
        except:
            messages.error(request,"Erreur d'envoi")
            return HttpResponseRedirect(reverse("feedback"))

def chatbot(request):
    classes = Class.objects.all()
    return render(request,"parent_template/chatbot.html" , { "classes": classes})
def chatbot_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        parent = Parents.objects.get(admin=request.user.id)
        reclamation = request.POST.get("reclamation")
        class_id = parent.class_id
        chatbot=Chatbot(class_id=class_id, parent_id=parent, Type="aaa", reclamation=reclamation)
        chatbot.save()
        messages.success(request, "feedback envoyé")
        return HttpResponseRedirect(reverse("chatbot"))

def avertissement(request):
    student = Parents.objects.get(admin=request.user.id)
    avr = Advertisement.objects.all()
    matiere = Subjects.objects.all()
    ens = Advertisement.objects.filter(parent_id=student)
    return render(request, "parent_template/avertissement.html",{"ens": ens ,"avr": avr, "matiere": matiere})
def profil(request):
    student = Parents.objects.get(admin=request.user.id)
    return render(request, "parent_template/profil.html",{"student": student })


def manage_schedule(request):
    classes = Class.objects.all()
    return render(request, "parent_template/manage_schedule.html", {"classes": classes})


def schedule_open(request):
    emploi = Schedule.objects.all()

    class_id = request.POST.get("class_id")
    year = request.POST.get("year")
    class_obj = Class.objects.get(id=class_id)
    global class_id_val

    def class_id_val():
        return class_obj

    global year_val

    def year_val():
        return year

    ok = False
    for ep in emploi:
        if (ep.class_id == class_obj) and (ep.year == year):
            ok = True
            return HttpResponseRedirect("schedule")
    if ok == False:
        messages.error(request, "On a pas trouvé l'emploi")
        return HttpResponseRedirect("manage_schedule")


def schedule(request):
    emploi = Schedule.objects.all()
    class_obj = class_id_val()
    year = year_val()
    liste1 = []
    liste2 = []
    liste3 = []
    liste4 = []
    liste5 = []
    n = 1
    for ep in emploi:
        if (ep.class_id == class_obj) and (ep.year == year):

            if n <= 6:
                liste1.append(ep)
                n = n + 1
            elif 6 < n <= 12:
                liste2.append(ep)
                n = n + 1
            elif 12 < n <= 18:
                liste3.append(ep)
                n = n + 1
            elif 18 < n <= 24:
                liste4.append(ep)
                n = n + 1
            else:
                liste5.append(ep)
                n = n + 1

    return render(request, "parent_template/schedule.html",
                  {"class_obj": class_obj, "year": year, "liste1": liste1, "liste2": liste2, "liste3": liste3,
                   "liste4": liste4, "liste5": liste5})


def manage_exam_open(request):
    emploi = ExamSchedule.objects.all()

    class_id = request.POST.get("class_id")
    num = request.POST.get("num")
    class_obj = Class.objects.get(id=class_id)
    global class_id_val1

    def class_id_val1():
        return class_obj

    global num_val1

    def num_val1():
        return num

    ok = False
    for ep in emploi:
        if (ep.class_id == class_obj) and (ep.num == num):
            ok = True
            return HttpResponseRedirect("manage_exam")
    if ok == False:
        messages.error(request, "On a pas trouvé calendrier")
        return HttpResponseRedirect("manage_exam_day")


def manage_exam(request):
    emploi = ExamSchedule.objects.all()
    class_obj = class_id_val1()
    num = num_val1()
    liste = []
    liste1 = []
    liste2 = []
    liste3 = []
    liste4 = []
    liste5 = []

    n = 0
    for ep in emploi:
        if (ep.class_id == class_obj) and (ep.num == num):
            nb = ep.day_nbr_id.day_nbr
            if n < nb:
                liste1.append(ep)
                n = n + 1
            elif nb <= n < nb * 2:
                liste2.append(ep)
                n = n + 1
            elif nb * 2 <= n < nb * 3:
                liste3.append(ep)
                n = n + 1
            elif nb * 3 <= n < nb * 4:
                liste4.append(ep)
                n = n + 1
            else:
                liste5.append(ep)
                n = n + 1
    n = 0
    for ep in liste1:
        if n < nb:
            liste.append(ep)
            n = n + 1

    return render(request, "parent_template/manage_exam.html",
                  {"class_obj": class_obj, "num": num, "liste": liste, "liste1": liste1, "liste2": liste2,
                   "liste3": liste3, "liste4": liste4, "liste5": liste5})
def manage_exam_day(request):
    classes=Class.objects.all()
    return render(request,"parent_template/manage_exam_day.html",{"classes":classes})