from django.urls import path
from .views import ReportListView, ReportDetailView, ReportEditView, ReportDeleteView,ReportCreateView

urlpatterns = [
    path('', ReportListView.as_view(), name='report_list'),
    path('<int:pk>/edit/', ReportEditView.as_view(), name='report_edit'),
    path('<int:pk>', ReportDetailView.as_view(), name='report_detail'),
    path('<int:pk>/delete/', ReportDeleteView.as_view(), name='report_delete'),
    path('upload/',ReportCreateView.as_view(), name='report_create'),
]
