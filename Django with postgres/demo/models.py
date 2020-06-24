from django.db import models

# Create your models here.
class Varsity(models.Model):
    name = models.CharField(max_length=200)
    loaction = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    seats = models.IntegerField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    varsity = models.ForeignKey(Varsity,on_delete=models.CASCADE,related_name="teacher")
    department = models.ForeignKey(Department, on_delete=models.CASCADE,related_name="teacher")
    years_of_service = models.IntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    sessions = (
            ("2016-17","2016-17"),
            ("2017-18","2017-18"),
            ("2018-19","2018-19"),
            ("2019-20","2019-20"),
        )

    name = models.CharField(max_length=200)
    reg_no = models.IntegerField()
    department=models.ForeignKey(Department,on_delete=models.CASCADE,related_name="student")
    varsity=models.ForeignKey(Varsity,on_delete=models.CASCADE,related_name="student")
    session = models.CharField(max_length=200,choices=sessions)
    def __str__(self):
        return self.name

