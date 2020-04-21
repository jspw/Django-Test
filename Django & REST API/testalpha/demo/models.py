from django.db import models

# Create your models here.

class GlobalSerial(models.Model):
    student_id = models.IntegerField()

class Varsity (models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class Department (models.Model):
    name = models.CharField(max_length=100)
    seats = models.IntegerField()

    def __str__(self):
        return self.name


class Teacher (models.Model):
    name = models.CharField(max_length=200)
    dept = models.ManyToManyField(Department,related_name="teacher")
    
    def __str__(self):
        return self.name
   
    

class Student(models.Model):
    student_id = models.OneToOneField(GlobalSerial, on_delete=models.CASCADE,null=True)
    
    name = models.CharField(max_length=200)
    reg_no = models.IntegerField()

    dept = models.ForeignKey(Department, on_delete=models.CASCADE,null=True,related_name="student")  #one to may relation!
    varsity = models.ForeignKey(Varsity, on_delete=models.CASCADE,null=True,related_name="student")  #one to may relation!

    birth = models.DateField()
    comment = models.CharField(max_length=500,blank=True)

    def __str__(self):
        return self.name



