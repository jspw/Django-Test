from django.contrib import admin
from demo.models import Student,Department,Varsity,Teacher,GlobalSerial


# Register your models here.
@admin.register(GlobalSerial)
class golAdmin(admin.ModelAdmin):
    fields = ["student_id",]

@admin.register(Varsity)
class varAdmin(admin.ModelAdmin):
    fields = ["name","location",]

    search_fields=["name","location"]


@admin.register(Department)
class deptAdmin(admin.ModelAdmin):
    fields = ["name","seats",]

    search_fields=["name"]

@admin.register(Student)
class stdAdmin(admin.ModelAdmin):
    fields = ["student_id","name","reg_no","dept","varsity","birth","comment"]

    search_fields=["name"]

@admin.register(Teacher)
class tecAdmin(admin.ModelAdmin):
    fields = ["name","dept",]

    search_fields=["name"]


