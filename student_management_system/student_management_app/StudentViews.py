import datetime
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from student_management_app.models import Parents, Courses, Specification, CustomUser, Attendance, Attendance_Report, Teachers, Homework, Exams, Facturation, FeedBackParent, Chatbot, Class

def student_home(request):
    parent_obj=Parents.objects.get(admin=request.user.id)
    global parent
    def parent():
        return parent_obj
    attendance_total=Attendance_Report.objects.filter(parent_id=parent_obj).count()
    attendance_present = Attendance_Report.objects.filter(parent_id=parent_obj,status=True).count()
    attendance_absent = Attendance_Report.objects.filter(parent_id=parent_obj,status=False).count()
    classe=Class.objects.get(id=parent_obj.class_id.id)
    subjects=Specification.objects.filter(class_id=classe).count()
    subject_name=[]
    data_present = []
    data_absent = []
    subject_data=Specification.objects.filter(class_id=parent_obj.class_id)
    for subject in subject_data:
        attendance=Attendance.objects.filter(subject_id=subject.id)
        attendance_present_count=Attendance_Report.objects.filter(attendance_id__in=attendance, status=True, parent_id=parent_obj).count()
        attendance_absent_count = Attendance_Report.objects.filter(attendance_id__in=attendance,status= False, parent_id=parent_obj).count()
        subject_name.append(subject.subject_id.subject_name)
        data_present.append(attendance_present_count)
        data_absent.append(attendance_absent_count)

        return render(request,"parent_template/student_home_template.html",{"parent": parent_obj,"attendance_total": attendance_total,"attendance_present": attendance_present,"attendance_absent": attendance_absent, "subjects":subjects , "data_name":subject_name,"data_present":data_present, "data_absent":data_absent})
def student_view_attendance(request):
    student=Parents.objects.get(admin=request.user.id)
    classe=Class.objects.get(id=student.class_id.id)
    subjects=Specification.objects.filter(class_id=classe)
    return render(request,"parent_template/student_view_attendance.html",{"subjects":subjects})
def student_view_attendance_post(request):
    subject_id=request.POST.get('subject')
    start_date=request.POST.get('start_date')
    end_date=request.POST.get('end_date')

    start_date_parse=datetime.datetime.strptime(start_date,"%Y-%m-%d").date()
    end_date_parse=datetime.datetime.strptime(end_date,"%Y-%m-%d").date()
    subject_obj=Specification.objects.get(id=subject_id)
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
        
        
       
        
        try:
            facture_model=Facturation(parent_id=parent)
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
    
    parent = Parents.objects.get(admin=request.user.id)
    
    return render(request,"parent_template/chatbot.html" , {"parent": parent})


def chatbot_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        parent = Parents.objects.get(admin=request.user.id)
        reclamation = request.POST.get("reclamation")
        classe=Class.objects.get(id=parent.class_id.id)
        chatbot=Chatbot(class_id=classe, parent_id=parent, type="aaaaa", reclamation=reclamation)
        chatbot.save()
           
        
