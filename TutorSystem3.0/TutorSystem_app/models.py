from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    TeacherID = models.CharField(max_length = 100)
    Username = models.ForeignKey(User)
    
    Age = models.CharField(max_length = 10)
    Sex = models.BooleanField(default=True)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length = 11)
    School = models.CharField(max_length = 50)
    #Photo = models.ImageField()
    Introduction = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return self.TeacherID

class Tutor_information(models.Model):
    Subject = models.CharField(max_length = 50)
    Grade = models.CharField(max_length = 50)
    Time = models.CharField(max_length = 50)
    Price = models.CharField(max_length = 50)
    TeacherID = models.ForeignKey(Teacher)
    def __unicode__(self):
        return self.Subject

class Student(models.Model):
    StudentID = models.CharField(max_length = 100)
    Username = models.ForeignKey(User)
    
    Grade = models.CharField(max_length = 50)    
    Sex = models.BooleanField(default=True)
    Email = models.CharField(max_length = 100)
    Phone = models.CharField(max_length = 11)
    #Photo = models.ImageField()
    
    def __unicode__(self):
        return self.StudentID

class Student_information(models.Model):
    Subject = models.CharField(max_length = 50)
    Time = models.CharField(max_length = 50)
    Address = models.CharField(max_length = 100)
    StudentID = models.ForeignKey(Student)
    
class Judge(models.Model):
    TeacherID = models.CharField(max_length = 100)
    StudentID = models.ForeignKey(Student)
    Content =  models.CharField(max_length = 100)

class Precontract(models.Model):
    PrecontractID = models.CharField(max_length = 100)
    TeacherID = models.CharField(max_length = 100)
    StudentID = models.CharField(max_length = 100)
    Subject = models.CharField(max_length = 100)
    Time = models.CharField(max_length = 100)
    State = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.PrecontractID