from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView
from . models import Diary
from . forms import DiaryForm
from django.urls import reverse_lazy
# Create your views here.

class IndexView(TemplateView):
    template_name = "diary/index.html"

class DiaryCreateVeiw(CreateView):
    template_name = "diary/diary_create.html"
    form_class = DiaryForm
    success_url = reverse_lazy("diary:diary_create_complete")

class DiaryCreateComplete(TemplateView):
    template_name = "diary/diary_create_complete.html"

class DiaryListView(ListView):
    template_name = "diary/diary_list.html"
    model = Diary

class DiaryDetailView(DetailView):
    template_name = "diary/diary_detail.html"
    model = Diary
