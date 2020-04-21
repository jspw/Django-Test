from rest_framework import serializers
from demo.models import Student,Teacher,Varsity,Department

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["name",]

class StudentSerializer(serializers.ModelSerializer):
    # var = VarsitySerializer(many=False)
    # teacher = TeacherSerializer(many=True)
    # department =Department(many=False)
    class Meta:
        model = Student
        fields = ["student_id","name","reg_no","dept","varsity","birth","comment",]

class MinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["id","name"]


class DepartmentSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=True)
    teacher = TeacherSerializer(many=True)
    class Meta:
        model = Department
        fields = ["name","seats","student","teacher"]


class VarsitySerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(many=False)
    class Meta:
        model = Varsity
        fields = ["name","location","department"]

