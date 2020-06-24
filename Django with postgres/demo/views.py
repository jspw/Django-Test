from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

class Index(ListView):
    template_name = "index.html"

    context_object_name = "info"

    def get_queryset(self):
        return super().get_queryset()