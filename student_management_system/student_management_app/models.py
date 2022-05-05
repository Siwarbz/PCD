from django.contrib.auth.models import AbstractUser

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save




# Create your models here.
class CustomUser(AbstractUser):
    user_type_data=((1,"Admin"),(2,"Teacher"),(3,"Parent"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Class(models.Model):
    id=models.AutoField(primary_key=True)
    class_name=models.CharField(max_length=255)
    level=models.IntegerField()
    objects=models.Manager() 

class Subjects_name(models.Model):
    id=models.AutoField(primary_key=True)
    subject_name=models.CharField(max_length=255)
    
    objects=models.Manager()   

  

class Courses(models.Model):
    id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    #le plus de rahma
    subject_name=models.CharField(max_length=255)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, default=1)
    file=models.FileField()
    description=models.CharField(max_length=25)

    
    objects=models.Manager()

class Teachers(models.Model):
     id=models.AutoField(primary_key=True)
     admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
     address=models.TextField()
     created_at=models.DateTimeField(auto_now_add=True)
     updated_at=models.DateTimeField(auto_now_add=True)
     
     objects=models.Manager()



class Specification(models.Model):
    id=models.AutoField(primary_key=True)
    subject_id=models.ForeignKey(Subjects_name,on_delete=models.CASCADE)
    teacher_id=models.ForeignKey(Teachers,on_delete=models.CASCADE)
    class_id=models.ForeignKey(Class,on_delete=models.CASCADE,default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


#specification===subjects






class Homework(models.Model):
    id = models.AutoField(primary_key=True)
    homework_name = models.CharField(max_length=255)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Specification, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
#ajoutés par rahma
    deadline = models.DateTimeField()
    description = models.CharField(max_length=255)
    subject_name = models.CharField(max_length=255)
    file = models.FileField()
    objects = models.Manager()

class Exams(models.Model):
    id=models.AutoField(primary_key=True)
    exam_name=models.CharField(max_length=255)
    mark=models.IntegerField()
    class_id=models.ForeignKey(Class,on_delete=models.CASCADE)
    teacher_id=models.ForeignKey(Teachers,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(Specification,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    remarque = models.CharField(max_length=255) 
    objects=models.Manager()
class Parents(models.Model):
    id=models.AutoField(primary_key=True)
    kid_name=models.CharField(max_length=255)
    kid_gender=models.CharField(max_length=255)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.TextField()
    class_id=models.ForeignKey(Class,on_delete=models.DO_NOTHING)
   
    session_start_year=models.DateField()
    session_end_year=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Facturation(models.Model):
    id = models.AutoField(primary_key=True)
    
    parent_id = models.ForeignKey(Parents, on_delete=models.DO_NOTHING)
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Note(models.Model):
    id=models.AutoField(primary_key=True)
    exam_name=models.CharField(max_length=255)
    note=models.IntegerField()
    parent_id=models.ForeignKey(Parents,on_delete=models.DO_NOTHING)
    class_id=models.ForeignKey(Class,on_delete=models.DO_NOTHING)
    subject_id=models.ForeignKey(Subjects_name,on_delete=models.DO_NOTHING)
    teacher_id=models.ForeignKey(Teachers,on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class Attendance(models.Model):
    id=models.AutoField(primary_key=True) 
    subject_id=models.ForeignKey(Specification,on_delete=models.DO_NOTHING)
    Attendance_date=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    



class Attendance_Report(models.Model): 
    id=models.AutoField(primary_key=True)
    parent_id=models.ForeignKey(Parents,on_delete=models.DO_NOTHING)
    attendance_id=models.ForeignKey(Attendance,on_delete=models.CASCADE)
    status=models.BooleanField(default=False) 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()





class FeedBackParent(models.Model):
    id=models.AutoField(primary_key=True)
    parent_id=models.ForeignKey(Parents,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=255)
    feedback_reply=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()  

class FeedBackTeacher(models.Model):
    id=models.AutoField(primary_key=True)
    teacher_id=models.ForeignKey(Teachers,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=255)
    feedback_reply=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()    


class NotificationParent(models.Model):
    id=models.AutoField(primary_key=True)
    parent_id=models.ForeignKey(Parents,on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()  

class NotificationTeacher(models.Model):
    id=models.AutoField(primary_key=True)
    teacher_id=models.ForeignKey(Teachers,on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()  

class Schedule(models.Model):
     id=models.AutoField(primary_key=True)
     class_id=models.ForeignKey(Class,on_delete=models.DO_NOTHING)
     teacher_id=models.ForeignKey(Teachers,on_delete=models.DO_NOTHING)
     subject_id=models.ForeignKey(Subjects_name,on_delete=models.DO_NOTHING)
     year=models.TextField()
     session_time=models.TextField()
     session_day=models.TextField()
     created_at=models.DateTimeField(auto_now_add=True)
     updated_at=models.DateTimeField(auto_now_add=True)
     
     objects=models.Manager()  
class Days_nbr(models.Model):
    id=models.AutoField(primary_key=True)
    day_nbr=models.IntegerField()

class ExamSchedule(models.Model):
     id=models.AutoField(primary_key=True)
     class_id=models.ForeignKey(Class,on_delete=models.DO_NOTHING)
     
     subject_id=models.ForeignKey(Subjects_name,on_delete=models.DO_NOTHING)
     date=models.DateField()
     session_time=models.TextField()
     num=models.TextField()
     day_nbr_id=models.ForeignKey(Days_nbr,on_delete=models.DO_NOTHING)
     created_at=models.DateTimeField(auto_now_add=True)
     updated_at=models.DateTimeField(auto_now_add=True)
     
     objects=models.Manager()  

class Chatbot(models.Model):
     id=models.AutoField(primary_key=True)
     parent_id=models.ForeignKey(Parents,on_delete=models.DO_NOTHING)
     class_id=models.ForeignKey(Class,on_delete=models.DO_NOTHING)
     
     type=models.TextField()
     reclamation=models.TextField()
     
     created_at=models.DateTimeField(auto_now_add=True)
     updated_at=models.DateTimeField(auto_now_add=True)
     
     objects=models.Manager()       

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            Admin.objects.create(admin=instance)
        if instance.user_type==2:
            Teachers.objects.create(admin=instance)
        if instance.user_type==3:
            Parents.objects.create(admin=instance,class_id=Class.objects.get(id=1),session_start_year='2022-01-01',session_end_year='2023-01-01',address="",kid_gender="")

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.admin.save()
    if instance.user_type==2:
        instance.teachers.save()
    if instance.user_type==3:
        instance.parents.save()
