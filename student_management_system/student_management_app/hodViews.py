from curses import nocbreak
from logging.config import listen
from mailbox import NoSuchMailboxError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from student_management_app.models import CustomUser, Teachers,Class,Parents,Subjects,Specification
from student_management_app.models import Schedule,Days_nbr,ExamSchedule,Chatbot,Facturation, Note

def admin_home(request):
   nbr1=Parents.objects.all().count()
   nbr2=Teachers.objects.all().count()
   nbr3=Class.objects.all().count()
   nbr4=Chatbot.objects.all().count()
     

   return render(request,"hod_template/home_content.html",{"nombre_eleve":nbr1,"nombre_ens":nbr2,"nombre_classe":nbr3,"nb":nbr4})




def add_teacher(request):
    return render(request,"hod_template/add_teacher_template.html") 



def add_teacher_save(request):
    if request.method!="POST":
       return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
       first_name=request.POST.get("first_name")
       last_name=request.POST.get("last_name")
       username=request.POST.get("username")
       password=request.POST.get("password")
       email=request.POST.get("email")
       address=request.POST.get("address")
       try:
          user=CustomUser.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password,email=email,user_type=2)
          user.teachers.address=address
          user.save()
          messages.success(request,"Teacher is Sucessfully Added")
          
          return HttpResponseRedirect("/add_teacher")

       except:
          messages.error(request,"Failed to add a teacher")
          return HttpResponseRedirect("/add_teacher")

       
def exam_calendar(request):
   return render(request,"hod_template/exam_calendar.html")
       
          
 

def add_class(request):
    return render(request,"hod_template/add_class_template.html") 


def add_class_save(request):
    if request.method!="POST":
       return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
       class_name=request.POST.get("class_name")
       level=request.POST.get("level")
       
       try:
          classe=Class(class_name=class_name,level=level)
          classe.save()
          messages.success(request,"Class is Sucessfully Added")
          
          return HttpResponseRedirect("/add_class")

       except:
          messages.error(request,"Failed to add a class")
          return HttpResponseRedirect("/add_class")


def add_subject(request):
    
    return render(request,"hod_template/add_subject_template.html") 

def add_subject_save(request):
    if request.method!="POST":
       return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
       subject_name=request.POST.get("subject_name")
       
       
       try:
          subject=Subjects(subject_name=subject_name)
          subject.save()
          messages.success(request,"subject is Sucessfully Added")
          
          return HttpResponseRedirect("/add_subject")

       except:
          messages.error(request,"Failed to add a subject")
          return HttpResponseRedirect("/add_subject")



def add_specification(request):
    classes=Class.objects.all()
    teachers=Teachers.objects.all()
    subjects=Subjects.objects.all()
    return render(request,"hod_template/add_specification.html",{"classes":classes ,"teachers":teachers,"subjects":subjects}) 


def add_specification_save(request):
    if request.method!="POST":
       return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
       subject_id=request.POST.get("subject_id")
       class_id=request.POST.get("class_id")
       teacher_id=request.POST.get("teacher_id")
       
       
       try:
          class_obj=Class.objects.get(id=class_id)
          subject_obj=Subjects.objects.get(id=subject_id)
          teacher_obj=Teachers.objects.get(id=teacher_id)
          specification=Specification(subject_id=subject_obj,teacher_id=teacher_obj,class_id=class_obj)
          
          specification.save()
          messages.success(request,"Specification is Sucessfully Added")
          
          return HttpResponseRedirect("/add_specification")

       except:
          messages.error(request,"Failed to add a specification")
          return HttpResponseRedirect("/add_specification")

def add_parent(request):
    classes=Class.objects.all()
    return render(request,"hod_template/add_parent_template.html",{"classes":classes}) 







def add_parent_save(request):
    if request.method!="POST":
       return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
       first_name=request.POST.get("first_name")
       last_name=request.POST.get("last_name")
       username=request.POST.get("username")
       password=request.POST.get("password")
       email=request.POST.get("email")
       address=request.POST.get("address")
       kid_name=request.POST.get("kid_name")
       kid_gender=request.POST.get("kid_gender")
       session_start_year=request.POST.get("session_start_year")
       session_end_year=request.POST.get("session_end_year")
       class_id=request.POST.get("class_id")
       try:

          user=CustomUser.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password,email=email,user_type=3)
          user.parents.address=address 
          class_obj=Class.objects.get(id=class_id)
          user.parents.kid_name=kid_name
          user.parents.kid_gender=kid_gender
          user.parents.session_start_year=session_start_year
          user.parents.session_end_year=session_end_year
          user.parents.class_id=class_obj
          user.save()
          messages.success(request,"Parent is Sucessfully Added")
          
          return HttpResponseRedirect("/add_parent")
       except:
          messages.error(request,"Failed to add a parent")
          return HttpResponseRedirect("/add_parent")
def manage_teacher(request):
    teachers=Teachers.objects.all()
    return render(request,"hod_template/manage_teacher_template.html", {"teachers":teachers}) 


    
    
    


def manage_parent(request):
    parents=Parents.objects.all()
    fact=Facturation.objects.all()
    
    l=[]
    liste=[]
    for f in fact:
          obj=f.parent_id
          l.append(obj) 
    
    for p in parents:
          if p in l:
             liste.append(p)
    
    
    
    return render(request,"hod_template/manage_parent_template.html", {"parents":parents,"fact":fact,"liste":liste}) 

def manage_class(request):
    classes=Class.objects.all()
    
    return render(request,"hod_template/manage_class_template.html", {"classes":classes}) 

def manage_subject(request):
    subjects=Subjects.objects.all()
    
    return render(request,"hod_template/manage_subject_template.html", {"subjects":subjects}) 

def manage_specification(request):
    specification=Specification.objects.all()
    
    return render(request,"hod_template/manage_specification.html", {"specification":specification}) 

def time_management(request):
    teachers=Teachers.objects.all()
    subjects=Subjects.objects.all()
    classes=Class.objects.all()
    return render(request,"hod_template/time_management.html",{"subjects":subjects,"teachers":teachers , "classes":classes}) 

def time_management_save(request):
    if request.method!="POST":
       return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
       days=["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi"]
       times=["08:00/09:50","10:10/12:00","12:00/13:00","13:00/14:50	","15:10/17:00"]
       class_id=request.POST.get("class_id")
       year=request.POST.get("year")
       n=1
       for i in range(5):
          time=times[i]
          for j in range(6):
             
             day=days[j]
             subject_id=request.POST.get("subject_id"+str(n))
             teacher_id=request.POST.get("teacher_id"+str(n))
             class_obj=Class.objects.get(id=class_id)
             teacher_obj=Teachers.objects.get(id=teacher_id)
             subject_obj=Subjects.objects.get(id=subject_id)
             session=Schedule(class_id=class_obj,teacher_id=teacher_obj,subject_id=subject_obj,year=year,session_time=time,session_day=day)
             session.save()
             n=n+1
       try:
          messages.success(request,"Schedule is Sucessfully Added")
          return HttpResponseRedirect("/time_management")
       except:
          messages.error(request,"Failed to add a schedule")
          return HttpResponseRedirect("/time_management")   

       
def manage_schedule(request):
    classes=Class.objects.all()
    return render(request,"hod_template/manage_schedule.html",{"classes":classes}) 



def schedule_open(request):
   emploi=Schedule.objects.all()
   
   class_id=request.POST.get("class_id")
   year=request.POST.get("year")
   class_obj=Class.objects.get(id=class_id)
   global class_id_val
   def class_id_val():
      return class_obj
   global year_val
   def year_val():
      return year
   ok=False
   for ep in emploi:
        if (ep.class_id==class_obj) and (ep.year==year) :
           ok=True
           return HttpResponseRedirect("/schedule")
   if ok==False:
          messages.error(request,"On a pas trouvé l'emploi")
          return HttpResponseRedirect("/manage_schedule")
       
def schedule(request):
      emploi=Schedule.objects.all()
      class_obj=class_id_val()
      year=year_val()
      liste1=[]
      liste2=[]
      liste3=[]
      liste4=[]
      liste5=[]
      n=1
      for ep in emploi:
         if (ep.class_id==class_obj) and (ep.year==year) :

            if n<=6:
               liste1.append(ep)
               n=n+1
            elif 6<n<=12:
               liste2.append(ep)
               n=n+1
            elif 12<n<=18:
               liste3.append(ep)
               n=n+1
            elif 18<n<=24:
               liste4.append(ep)
               n=n+1
            else: 
               liste5.append(ep)
               n=n+1
            

      return render(request,"hod_template/schedule.html",{"class_obj":class_obj,"year":year,"liste1":liste1,"liste2":liste2,"liste3":liste3,"liste4":liste4,"liste5":liste5})  
   
           
def add_exam_days(request):
    classes=Class.objects.all()
    
    return render(request,"hod_template/add_exam_days.html", {"classes":classes}) 

def add_exam_days_save(request):
   if request.method!="POST":
       return HttpResponse("<h2>Method Not Allowed</h2>")
   else:
       day=request.POST.get("day_nbr")
       global nbr 
       def nbr():
           return day
       
       
       try:
          days=Days_nbr(day_nbr=day)
          global jour
          def jour():
           return days
          days.save()
          
          
          return HttpResponseRedirect("/add_exam")

       except:
          messages.error(request,"Failed to add a nbr")
          return HttpResponseRedirect("/add_exam_days")
   
       

def add_exam(request):
    classes=Class.objects.all()
    teachers=Teachers.objects.all()
    subjects=Subjects.objects.all()
    nbr_jr=nbr()
    liste1=[]
    liste2=[]
    liste3=[]
    liste4=[]
    liste5=[]
    liste6=[]
    for i in range(int(nbr_jr)):
       liste1.append("date"+str(i))

    for i in range(int(nbr_jr)):
       liste2.append("subject_id"+str(i))

    for i in range(int(nbr_jr),int(nbr_jr)*2):
       liste3.append("subject_id"+str(i))

    for i in range(int(nbr_jr)*2,int(nbr_jr)*3):
       liste4.append("subject_id"+str(i))
   
    for i in range(int(nbr_jr)*3,int(nbr_jr)*4):
       liste5.append("subject_id"+str(i))

    for i in range(int(nbr_jr)*4,int(nbr_jr)*5):
       liste6.append("subject_id"+str(i))
    

    return render(request,"hod_template/add_exam.html", {"liste1":liste1,"liste2":liste2,"liste3":liste3,"liste4":liste4,"liste5":liste5,"liste6":liste6,"classes":classes,"teachers":teachers , "subjects":subjects}) 
   
def add_exam_save(request):
   if request.method!="POST":
       return HttpResponse("<h2>Method Not Allowed</h2>")
   else:
       
       times=["08:00/09:50","10:10/12:00","12:00/13:00","13:00/14:50	","15:10/17:00"]
       class_id=request.POST.get("class_id")
       class_obj=Class.objects.get(id=class_id)
       
       num=request.POST.get("num")
       n=0
       nb=nbr()
       for i in range(5):
          time=times[i]
          for j in range(int(nb)):
             
             day=request.POST.get("date"+str(j))
             subject_id=request.POST.get("subject_id"+str(n))
             subject_obj=Subjects.objects.get(id=subject_id)
             
             
             
             
             session=ExamSchedule(class_id=class_obj,subject_id=subject_obj,num=num,day_nbr_id=jour(),session_time=time,date=day)
             session.save()
             n=n+1
       try:
          messages.success(request,"Calendrier ajoutée")
          return HttpResponseRedirect("/add_exam_days")
       except:
          messages.error(request,"Calendrier non ajoutée")
          return HttpResponseRedirect("/add_exam_days")   


def facturation(request):
    parents=Parents.objects.all()
    fact=Facturation.objects.all()
    

    return render(request,"hod_template/facturation.html",{"parents":parents},{"fact":fact}) 

def add_note(request):
    subjects=Subjects.objects.all()
    classes=Class.objects.all()
    return render(request,"hod_template/add_note.html",{ "classes":classes,"subjects":subjects}) 

def add_note_save(request):
    classes=Class.objects.all()
    if request.method!="POST":
       return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
      
       class_id=request.POST.get("class_id")
       class_obj=Class.objects.get(id=class_id)
       global cl_obj
       def cl_obj():
          return class_obj
       
       if class_obj in classes:
          
           return HttpResponseRedirect("/remplir_classe_note")
       else:
          messages.error(request,"on a pas trouvé cette classe")
          return HttpResponseRedirect("/add_note") 

def remplir_classe_note(request):
   teachers=Teachers.objects.all()
   subjects=Subjects.objects.all()
   parents=Parents.objects.all()
   class_id=cl_obj()
   liste=[]
   liste4=[]
   for parent in parents:
      if parent.class_id==class_id:
         liste.append(parent)
         liste4.append(parent.id)
   liste2=[]
   for i in range(len(liste)):
          liste2.append("note"+str(i))
   global liste1
   def liste1():
      return liste
   global liste3
   def liste3():
      return liste2  
   global liste5
   def liste5():
      return liste4     

   return render(request,"hod_template/remplir_classe_note.html",{"subjects":subjects,"teachers":teachers , "class_obj":class_id , "parents":parents,"liste":liste,"liste1":liste3()})


def remplir_note_save(request):
    
    if request.method!="POST":
       return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
       
       teacher_id=request.POST.get("teacher_id")
       subject_id=request.POST.get("subject_id")
       teacher_obj=Teachers.objects.get(id=teacher_id)
       subject_obj=Subjects.objects.get(id=subject_id)
       notede=request.POST.get("note")
       list1=liste1()
       list3=liste3()
       class_obj=cl_obj()
       list5=liste5()
      
                   
       for i in range(len(list1)):
          
        
             
             
             note=request.POST.get(list3[i])
             parent_obj=Parents.objects.get(id=list5[i])
             
             session=Note(parent_id=parent_obj,class_id=class_obj,teacher_id=teacher_obj,subject_id=subject_obj,note=note,exam_name=notede)
             session.save()
             
       try:
          messages.success(request,"Les notes sont ajoutées")
          return HttpResponseRedirect("/add_note")
       except:
          messages.error(request,"Erreur")
          return HttpResponseRedirect("/add_note")   
def manage_note(request):
    classes=Class.objects.all()
    subjects=Subjects.objects.all()
    return render(request,"hod_template/manage_note.html",{"classes":classes ,"subjects":subjects}) 



def manage_note_save(request):
   note=Note.objects.all()
   class_id=request.POST.get("class_id")
   subject_id=request.POST.get("subject_id")
   subject_obj=Subjects.objects.get(id=subject_id)
   class_obj=Class.objects.get(id=class_id)
   global class_id_val
   def class_id_val():
      return class_obj
   global subject_id_val
   def subject_id_val():
      return subject_obj
   ok=False
   
   for nt in note:
        if (nt.class_id==class_obj) and (nt.subject_id==subject_obj) :
           ok=True
           
           return HttpResponseRedirect("/manage_note_view")
   if ok==False:
          messages.error(request,"Vous avez pas inserez les notes de cette matière")
          return HttpResponseRedirect("/manage_note")

def manage_note_view(request):  
    classes=Class.objects.all()
    subjects=Subjects.objects.all()
    note=Note.objects.all()
    class_id=class_id_val()
    subject_id=subject_id_val()
    liste1=[]
    liste2=[]
    liste3=[]
    liste=[]
    liste0=[]
    for nt in note:
       if nt.class_id==class_id and nt.subject_id==subject_id :
          liste0.append(nt)
          teacher_id=nt.teacher_id
    n=0
    for nt in liste0:
       if n<len(liste0)/3:
             liste.append(nt)
       n=n+1
    

    for nt in liste0:
       if nt.exam_name=="Controle" :
          liste1.append(nt)
       if nt.exam_name=="Orale" :
          liste2.append(nt)  
       if nt.exam_name=="Examen" :
          liste3.append(nt)    
    return render(request,"hod_template/manage_note_view.html",{"classes":classes ,"subjects":subjects,"note":note,"subject_id":subject_id,"class_id":class_id,"teacher_id":teacher_id,"liste":liste,"liste1":liste1,"liste2":liste2,"liste3":liste3})

def manage_exam_day(request):
    classes=Class.objects.all()
    return render(request,"hod_template/manage_exam_day.html",{"classes":classes}) 



def manage_exam_open(request):
   emploi=ExamSchedule.objects.all()
   
   class_id=request.POST.get("class_id")
   num=request.POST.get("num")
   class_obj=Class.objects.get(id=class_id)
   global class_id_val1
   def class_id_val1():
      return class_obj
   global num_val1
   def num_val1():
      return num
   ok=False
   for ep in emploi:
        if (ep.class_id==class_obj) and (ep.num==num) :
           ok=True
           return HttpResponseRedirect("/manage_exam")
   if ok==False:
          messages.error(request,"On a pas trouvé calendrier")
          return HttpResponseRedirect("/manage_exam_day")
       
def manage_exam(request):
      emploi=ExamSchedule.objects.all()
      class_obj=class_id_val1()
      num=num_val1()
      liste=[]
      liste1=[]
      liste2=[]
      liste3=[]
      liste4=[]
      liste5=[]
      
      n=0
      for ep in emploi:
         if (ep.class_id==class_obj) and (ep.num==num) :
            nb=ep.day_nbr_id.day_nbr
            if n<nb:
               liste1.append(ep)
               n=n+1
            elif nb<=n<nb*2:
               liste2.append(ep)
               n=n+1
            elif nb*2<=n<nb*3:
               liste3.append(ep)
               n=n+1
            elif nb*3<=n<nb*4:
               liste4.append(ep)
               n=n+1
            else: 
               liste5.append(ep)
               n=n+1
      n=0
      for ep in liste1:
         if n<nb:
            liste.append(ep)
            n=n+1
            

      return render(request,"hod_template/manage_exam.html",{"class_obj":class_obj,"num":num,"liste":liste,"liste1":liste1,"liste2":liste2,"liste3":liste3,"liste4":liste4,"liste5":liste5})  
     
       
def manage_chatbot(request):
    chatbot=Chatbot.objects.all()
    chatbot.reverse()
    return render(request,"hod_template/chatbot.html",{"chatbot":chatbot}) 

     
       
      
       
    
    
