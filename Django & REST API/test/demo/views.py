from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book,Author,Number

#rest framework
from rest_framework import viewsets
from .serializers import BookSerializer,BookMinSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.

class index(View):
    # books = Book.objects.filter(Price=500)
    books = Book.objects.all()
    my_dict= {"book":books,}
    def get(self,request):
        return render(request,'demo/index.html',self.my_dict)


#serializer for drf

class BookViewSet(viewsets.ModelViewSet):
    serializer_class= BookMinSerializer

    queryset = Book.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


    def retrieve(self,request,*args ,**kwargs):
        instance=self.get_object()
        serializer=BookSerializer(instance)
        return Response(serializer.data)


    