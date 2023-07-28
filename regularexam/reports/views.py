from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Report

# Create your views here.
class ReportListView(ListView):
    template_name = 'report_list.html'
    model = Report

class ReportEditView(UpdateView):
    model = Report
    template_name = 'report_edit.html'
    fields = (
        'title',
        'body',
        'additional_materials',
    )

class ReportDeleteView(DeleteView):
    model = Report
    template_name = 'report_delete.html'
    success_url = reverse_lazy('report_list')
class ReportDetailView(DetailView):
    model = Report
    template_name = 'report_detail.html'

class ReportCreateView(CreateView):
    model = Report
    template_name = 'report_create.html'
    fields = (
        'title',
        'body',
        'author',
        'additional_materials',
        'common_vulnerability_scoring_system',
    )