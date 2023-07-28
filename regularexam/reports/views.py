from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Report


# Create your views here.
class ReportListView(ListView):
    template_name = 'report_list.html'
    model = Report


class ReportEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Report
    template_name = 'report_edit.html'
    fields = (
        'title',
        'body',
        'additional_materials',
    )

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ReportDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Report
    template_name = 'report_delete.html'
    success_url = reverse_lazy('report_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user



class ReportDetailView(DetailView):
    model = Report
    template_name = 'report_detail.html'


class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    template_name = 'report_create.html'
    fields = (
        'title',
        'body',
        'additional_materials',
        'common_vulnerability_scoring_system',
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
