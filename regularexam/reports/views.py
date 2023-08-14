from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Report
from .forms import CommentForm


# Create your views here.
class ReportListView(ListView):
    template_name = 'report_list.html'
    context_object_name = 'reports'
    model = Report
    queryset = Report.objects.all()
    paginate_by = 3


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
            form = CommentForm(request.POST, None)
            if form.is_valid() and request.user.is_authenticated:
                comment = form.save(commit=False)
                comment.report = self.get_object()
                comment.author = self.request.user
                comment.save()
                return redirect('report_detail', pk=comment.report.pk)
            else:
                return redirect('login')


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


