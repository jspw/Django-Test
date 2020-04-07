from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from . import  models
# Create your views here.


class IndexView(TemplateView):
    template_name = 'adv_app/index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme']='Basic Injection'

        return context


class SchoolListView(ListView):
    context_object_name = 'school_list'
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'adv_app/school_detail.html'

