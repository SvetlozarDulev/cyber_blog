from django.urls import path
from .views import HomePageView,EducationView,EducationList, GiveBestAdviceView, AdvicesList

urlpatterns = [
    path('',HomePageView.as_view(),name="home"),
    path('create-education/',EducationView.as_view(), name='education'),
    path('education-materials/',EducationList.as_view(), name='education-list'),
    path('write-advice/', GiveBestAdviceView.as_view(),name='write-advice'),
    path('advice-list/', AdvicesList.as_view(), name='best-advice'),
]