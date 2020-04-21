from django.shortcuts import render
from django.views import View
from demo.models import Student,Teacher,Varsity,Department
from django.views.generic import DetailView,ListView
# Create your views here.

# for rest framwork
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from demo.serializers import StudentSerializer,TeacherSerializer,VarsitySerializer,DepartmentSerializer,MinSerializer



class index(View):
    title = {"title":"Index"}

    def get(self,request):
        return render(request,'index.html',self.title)


class about(View):
    info={
        "title":"About",
        "name":"Shifat",
        "reg":"2017831017",
        "dept":"Software Engineering"

    }

    def get(self,request):
        return render(request,'about.html',self.info)


class List(ListView):
    # model = Student,Teacher
    template_name = 'list.html'
    context_object_name = 'info'
    
    # dist = {
    #     "students":student_model,
    #     "teachers":teacher_model
    # }
    # # print(fields)

    def get_queryset(self):
        queryset ={
            "students":Student.objects.all(),
            "teachers":Teacher.objects.all(),
            "department":Department.objects.all(),
            "varsity":Varsity.objects.all(),
        }

        return queryset


class Detail(DetailView):
    std = Student
    template_name = 'detail.html'
    context_object_name = 'student'
    queryset = Student.objects.all()


# for rest framework 

class ApiView(viewsets.ModelViewSet):
    # serializer_class = VarsitySerializer
    serializer_class = MinSerializer

    queryset = Department.objects.all()

    authentication_classed = (TokenAuthentication,)
    permission_classed = (IsAuthenticated)


    def retrieve(self,request,*args,**kwargs):
        instance = self.get_object()
        serializer = DepartmentSerializer(instance)
        return Response(serializer.data)

