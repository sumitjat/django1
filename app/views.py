from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,DeleteView
from django.http import HttpResponse
from app.models import Example
# Create your views here.

class Simple(View):
    def get(self,request0):
        return HttpResponse("<html><a href='/template/'>Test Link </a></html>")


class TemplateExam(TemplateView):
    template_name = 'template.html'


class ContextExam(TemplateView):
    template_name = 'context.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='sumit'
        context['age']=20
        return context


class ListExam(ListView):
    model = Example
    template_name = 'example_list.html'


class DetailExam(DetailView):

    model = Example
    template_name = 'example_detail.html'

class DeleteExam(DeleteView):
    model = Example
    success_url = reverse_lazy('main')
    # template_name = 'delete.html'

