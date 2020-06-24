from django.contrib import admin
from demo.models import Student,Teacher,Varsity,Department
# Register your models here.
@admin.register(Varsity)
class varsity(admin.ModelAdmin):
    fields =["name","loaction"]
    search_fields=["name"]


@admin.register(Department)
class department(admin.ModelAdmin):
    fields =["name","seats"]
    search_fields=["name"]


@admin.register(Teacher)
class teacher(admin.ModelAdmin):
    fields =["name","designation","varsity","department","years_of_service"]
    search_fields=["name"]


@admin.register(Student)
class student(admin.ModelAdmin):
    fields =["name","reg_no","varsity","department","session"]
    search_fields=["name"]






    